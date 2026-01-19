import csv
import statistics
from django.shortcuts import render
from django.views import View

class UploadView(View):

    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        file = request.FILES.get('csv_file')

        if not file or not file.name.endswith('.csv'):
            return render(request, 'upload.html', {'error': 'Please upload a valid CSV file'})

        decoded = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded)

        headers = next(reader)
        rows = list(reader)

        request.session['headers'] = headers
        request.session['rows'] = rows

        return render(request, 'table.html', {
            'headers': headers,
            'rows': rows
        })


class StatsView(View):

    def get(self, request):
        headers = request.session.get('headers')
        rows = request.session.get('rows')

        return render(request, 'stats.html', {
            'headers': headers
        })

    def post(self, request):
        column = request.POST.get('column')

        headers = request.session.get('headers')
        rows = request.session.get('rows')

        index = headers.index(column)
        values = [row[index] for row in rows if row[index] != '']

        numeric_values = []
        for v in values:
            try:
                numeric_values.append(float(v))
            except:
                pass

        result = {'column': column, 'missing': len(rows) - len(values)}

        if numeric_values:
            result['min'] = min(numeric_values)
            result['max'] = max(numeric_values)
            result['mean'] = round(statistics.mean(numeric_values), 2)
            result['median'] = statistics.median(numeric_values)
            result['mode'] = statistics.mode(numeric_values)
        else:
            result['mode'] = statistics.mode(values) if values else 'N/A'
            result['message'] = 'Not a numeric column'

        return render(request, 'stats.html', {
            'headers': headers,
            'result': result
        })

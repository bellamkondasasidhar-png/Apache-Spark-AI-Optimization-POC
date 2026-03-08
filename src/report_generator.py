import json
import datetime

class ReportGenerator:
    def __init__(self):
        self.optimizations = []
        self.failures = []
        self.performance_diagnostics = []

    def add_optimization(self, suggestion):
        self.optimizations.append(suggestion)

    def add_failure(self, reason):
        self.failures.append(reason)

    def add_performance_diagnostics(self, diagnostic):
        self.performance_diagnostics.append(diagnostic)

    def generate_json_report(self):
        report = {
            'date': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'optimizations': self.optimizations,
            'failures': self.failures,
            'performance_diagnostics': self.performance_diagnostics
        }
        return json.dumps(report, indent=4)

    def generate_html_report(self):
        html = '<html><head><title>Report</title></head><body>'
        html += '<h1>Optimization Report</h1>'
        html += '<h2>Date: ' + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + '</h2>'

        html += '<h3>Optimizations</h3><ul>'
        for suggestion in self.optimizations:
            html += f'<li>{suggestion}</li>'
        html += '</ul>'

        html += '<h3>Failures</h3><ul>'
        for reason in self.failures:
            html += f'<li>{reason}</li>'
        html += '</ul>'

        html += '<h3>Performance Diagnostics</h3><ul>'
        for diagnostic in self.performance_diagnostics:
            html += f'<li>{diagnostic}</li>'
        html += '</ul>'

        html += '</body></html>'
        return html

# Usage example:
# report_gen = ReportGenerator()
# report_gen.add_optimization('Use caching for frequently accessed data.')
# report_gen.add_failure('Connection timeout on database query.')
# report_gen.add_performance_diagnostics('Memory usage is within acceptable range.')
# print(report_gen.generate_json_report())
# print(report_gen.generate_html_report())

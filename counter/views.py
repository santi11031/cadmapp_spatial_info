from djust import LiveView

class CounterView(LiveView):
    template_name = 'counter/counter.html'

    def mount(self, request, **kwargs):
        """Called when the view is first loaded"""
        self.count = 0

    def increment(self):
        """Event handler - called when user clicks increment"""
        self.count += 1

    def decrement(self):
        """Event handler - called when user clicks decrement"""
        self.count -= 1

    def reset(self):
        """Event handler - called when user clicks reset"""
        self.count = 0

    def get_context_data(self, **kwargs):
        """Return context for template rendering"""
        return {'count': self.count}
6

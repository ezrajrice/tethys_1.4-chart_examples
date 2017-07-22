from tethys_sdk.base import TethysAppBase, url_map_maker


class ChartExamples(TethysAppBase):
    """
    Tethys app class for Chart Examples.
    """

    name = 'Chart Examples'
    index = 'chart_examples:home'
    icon = 'chart_examples/images/icon.gif'
    package = 'chart_examples'
    root_url = 'chart-examples'
    color = '#1abc9c'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='chart-examples',
                           controller='chart_examples.controllers.home'),
        )

        return url_maps
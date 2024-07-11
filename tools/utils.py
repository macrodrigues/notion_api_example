""" Functions and general tools """
# pylint: disable=W0718
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

chart_studio.tools.set_credentials_file(
    username='macrodrigues',
    api_key='huyGO3eArD6hipF0nOPo')


def gen_bar_domains(df_domains):
    """ Generate bar chart with domains. """
    data = go.Bar(
        x=df_domains['domain'],
        y=df_domains['count'],
        hovertemplate="""<br>Domain: %{x}
        <br>Counts: %{y}
        <extra></extra>""")

    layout = go.Layout(
                showlegend=False,  # table being used for legend
                template='plotly_white',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                yaxis=dict(
                    title='Counts',
                    showgrid=False,
                    side='left'),
                xaxis=dict(
                    title='Domains',
                    showgrid=False,
                    tickmode='array'))

    fig = go.Figure({'data': data, 'layout': layout})
    fig.update_layout(
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color='black'  # General text color
        )
    )

    fig.update_traces(marker_color='#9CDBA6')

    py.plot(fig, filename='notion-example', auto_open=True)

    with open("bar_domains.html", 'w', encoding='utf-8') as f:
        f.write(fig.to_html(
            include_plotlyjs='cdn',
            config={'displayModeBar': False}))

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output

app = dash.Dash(
	__name__, meta_tags=[{"name": "viewport", "content": "width=1000px"}]
)
server = app.server
app.title='My_dash_tutorial'

query_tp2node = {}
query_tp2node['disease'] = ['cancer','lung cancer','covid-19']
query_tp2node['gene'] = ['tp53','brac2','brac1']

# Create app layout
app.layout = html.Div([
	html.Div([
			html.Div([html.Div(id='left_textbox',className="title_text")],className='title_screen'),

			html.Div([#,className='img_screen'
			dcc.Dropdown(
				className="div-for-dropdown",
				id="disease-selector",
				options=[{"label": i, "value": i} for i in query_tp2node['disease']],value='',multi=False,
				placeholder="Select diseases",
			)]),

			html.Div([dcc.Dropdown(
				className="div-for-dropdown",
				id="gene-selector",
				options=[{"label": i, "value": i} for i in query_tp2node['gene']],value='',multi=False,
				placeholder="Select genes",
			)]),
			] ,className='left_screen'),

html.Div([html.Div(id='right_textbox',className="content_text")],className='right_screen'),
	])

@app.callback(Output('left_textbox', 'children'),[Input('disease-selector', 'value'),Input('gene-selector', 'value')]) #
def displayTapNodeData(disease,gene):
	return 'you selected gene: ' + gene

@app.callback(Output('right_textbox', 'children'),[Input('disease-selector', 'value'),Input('gene-selector', 'value')]) #
def displayTapNodeData(disease,gene):
	return disease+' is associated with '+ gene

if __name__ == "__main__":
	app.run_server(debug=True,host= '0.0.0.0',port='8052')

import flask
from flask import request,jsonify,render_template

app=flask.Flask(__name__)
app.config["DEBUG"]=True
countries=[
	{
		'name':'Afghanistan',
		'capital':'Kabul'
	},
	{
		'name':'Armenia',
		'capital':'Yerevan'
	},
	{
		'name':'Azerbaijan',
		'capital':'Baku'
	},
	{
		'name':'Bahrain',
		'capital':'Manama'
	},
	{
		'name':'Bangladesh',
		'capital':'Dhaka'
	},
	{
		'name':'Bhutan',
		'capital':'Thimphu'
	},
	{
		'name':'Brunel',
		'capital':'Bandar Seri Begawan'
	},
	{
		'name':'Cambodia',
		'capital':'Phnom Penh'
	},
	{
		'name':'China',
		'capital':'Beijing'
	},
	{
		'name':'Cyprus',
		'capital':'Nicosia'
	},
	{
		'name':'Georgia',
		'capital':'Tbilisi'
	},
	{
		'name':'India',
		'capital':'New Delhi'
	},
	{
		'name':'Indonesia',
		'capital':'Jakarta'
	},
	{
		'name':'Iran',
		'capital':'Tehran'
	},
	{
		'name':'Iraq',
		'capital':'Baghdad'
	},
	{
		'name':'Israel',
		'capital':'Jerusalem'
	},
	{
		'name':'Japan',
		'capital':'Tokyo'
	},
	{
		'name':'Jordan',
		'capital':'Amman'
	},
	{
		'name':'Kazakhstan',
		'capital':'Nur-Sultan'
	},
	{
		'name':'Kuwait',
		'capital':'Kuwait City'
	},
	{
		'name':'Kyrgyzstan',
		'capital':'Bishke;k'
	},
	{
		'name':'Laos',
		'capital':'Vientiane'
	},
	{
		'name':'Lebanon',
		'capital':'Beirut'
	},
	{
		'name':'Malasysia',
		'capital':'Kuala Lumpur'
	},
	{
		'name':'Maldives',
		'capital':'Male'
	},
	{
		'name':'Mongolia',
		'capital':'Ulaanbaatar'
	},
	{
		'name':'Manmar',
		'capital':'Naypyidaw'
	},
	{
		'name':'Nepal',
		'capital':'Kathmadu'
	},
	{
		'name':'North Korea',
		'capital':'Pyongyang'	
	},
	{
		'name':'Oman',
		'capital':'Muscat'
	},
	{
		'name':'Pakistan',
		'capital':'Islamabad'
	},
	{
		'name':'Palestine',
		'capital':'Jerusalem'
	},
	{
		'name':'Philippines',
		'capital':'Manila'
	},
	{
		'name':'Qatar',
		'capital':'Doha'
	},
	{
		'name':'Russia',
		'capital':'Moscow'
	},
	{
		'name':'Saudi Sradia',
		'capital':'Riyadh'
	},
	{
		'name':'Singapore',
		'capital':'Singapore'
	},
	{
		'name':'South Korea',
		'capital':'Seoul'
	},
	{
		'name':'Sri Lanka',
		'capital':'Sri Jayawardenepura Kotte'
	},
	{
		'name':'Syria',
		'capital':'Damascus'
	},
	{
		'name':'Taiwan',
		'capital':'Taipel'
	},
	{
		'name':'Tajikistan',
		'capital':'Dushande'
	},
	{
		'name':'Thailand',
		'capital':'Bangkok'
	},
	{
		'name':'Timor-Leste',
		'capital':'Dili'
	},
	{
		'name':'Turkey',
		'capital':'Ankara'
	},
	{
		'name':'Turkmenistan',
		'capital':'Ashgabat'
	},
	{
		'name':'United Arab Emirates',
		'capital':'Abu Dhadi'
	},
	{
		'name':'Uzbekistan',
		'capital':'Tashkent'
	},
	{
		'name':'Vietnam',
		'capital':'Hanoi'
	},
	{
		'name':'Yemen',
		'capital':'Sanaa'
	}

]

@app.route('/',methods=['GET'])
def home():
	return render_template('documentation.html')


@app.route('/api/v1/countries/all',methods=['GET'])
def api_all():
	return jsonify(countries)

@app.route('/api/v1/countries',methods=['POST'])
def api_country():
	if request.form.get("country") == "":
		return jsonify(countries)
	name = request.form.get("country").title()
	results=[]

	for country in countries:
		if(country['name']==name):
			results.append(country)
	return jsonify(results)		

if __name__ == "__main__":
	app.run()
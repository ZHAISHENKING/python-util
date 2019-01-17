class Demo(Resource):
    def get(self):
        a = [
            {"id": "1", "title": "浙江", "children": [{"title": "杭州", "id": "2"}]},
            {"id": "3", "title": "陕西", "children": [{"title": "西安", "id": "4"}]},
            {"id": "5", "title": "上海"}
        ]
        return make_response(render_template('demo.html', a=a))

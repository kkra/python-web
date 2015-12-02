import tornado.ioloop
import tornado.web


def allow_response(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Credentials", "true")
    self.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    self.set_header("Access-Control-Allow-Headers",
                    "Content-Type, Depth, User-Agent, X-File-Size, X-Requested-With, X-Requested-By, If-Modified-Since, X-File-Name, Cache-Control")


class MainJson(tornado.web.RequestHandler):

    def get(self):
        venta = {
            "total_values":["75,000","945","12/18","15","80%","+6","2","2","2","425","465"],
            "zonas":["a","b","c","d","f","g","h","i","j","k"],
            "pec":["Estable","Crítica","Estable","Productiva","Estable","Productiva","Crítica","Crítica","Productiva","Estable"],
            "leyenda":{
                "venta_yellow":{
                    "data_grafic":[452,3765,6736,3697,2078,7356,238,3875,4735,640],
                    "data_info":["452","3,765","6,736","3,697","2,078","7,356","238","3,875","4,735","640"]
                    },
                "pedidos_primary":{
                    "data_grafic":[452,3765,6736,3697,2078,7356,238,3875,4735,640],
                    "data_info":["452","3,765","6,736","3,697","2,078","7,356","238","3,875","4,735","640"]
                    },
                "ciclonuevas_success":{
                    "data_grafic":[452,3765,6736,3697,2078,7356,238,3875,4735,640],
                    "data_info":["452","3,765","6,736","3,697","2,078","7,356","238","3,875","4,735","640"]
                    }
                }
            }

        get_tipo = self.get_argument('tipo','venta')
        if get_tipo=="venta":
            self.write(venta)
        else:
            self.write(venta)

        allow_response(self)
        #self.write(json)

routers = [
    (r"/", MainJson),
    (r"/api/", MainJson),
    (r"/(.*)", tornado.web.StaticFileHandler,{'path': 'html/blogin'}),
    ]

application = tornado.web.Application(routers,debug=True)

if __name__ == "__main__":
    print("server run")
    application.listen(8088)
    tornado.ioloop.IOLoop.current().start()

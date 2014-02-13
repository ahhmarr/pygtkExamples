from gi.repository import Gtk
from gi.repository import Notify
class WindowGTK(Gtk.Window):
	def __init__(self,width,height):
		Gtk.Window.__init__(self,title="title")
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_size_request(width,height)
		self.box=Gtk.Box(spacing=6)
		self.add(self.box)
		self.b1=Gtk.Button(label="click me hommie")
		self.b1.set_size_request(10,20)
		self.b1.connect("clicked",self.run,"title","msg")
		self.box.pack_start(self.b1,True,True,0)
	def run(self,b1,title,msg):
		Notify.init("hello")
		n=Notify.Notification.new(title,msg,"error")
		n.show()

w=WindowGTK(400,320) #width and height
w.connect("delete-event",Gtk.main_quit)
w.show_all()
Gtk.main()



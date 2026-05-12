from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import string
import csv
import os

root = Tk()
root.geometry("400x400")
root.title("My Mega Mall")
root.configure(bg = "pink")
namee = Label(root, text="My Mega Mall", bg="pink", font=("Rockwell", 40))
namee.place(x=30,y=130)
curd = os.path.dirname(os.path.abspath(__file__))

n = 1
vc = ""
cc = ""
size_list = []
labels = []
ply = 250

manuf = 'Manufacturer.csv'
vendf= 'Vendor Details.csv'
allprof= "All Product Details.csv"
prof="Product Details.csv"
catf="Category Details.csv"

while True:
    if os.path.exists(manuf):
        break
    else:
        with open(manuf,"w") as a:
            obj = csv.writer(a)
            l=["Manufacturer Name","Code"]
            obj.writerow(l)

    if os.path.exists(vendf):
        break
    else:
        with open(vendf,"w") as a:
            obj = csv.writer(a)
            l=["Vendor Name","Address","GST Number"]
            obj.writerow(l)

    if os.path.exists(allprof):
        break
    else:
        with open(allprof,"w") as a:
            obj = csv.writer(a)
            l=["Category","Subcategory","Name","Colour","Weight","Brand Name","Vendor Name","Item Name","Item Code","Pickup Location","Return Duration","Cost Price","GST","Packing Cost","Total Cost","MRP","Direct Selling Price","Indirect Selling Price","Price on Other websites","Company Discount","Agent Discount","Profit Margin","Agent Comission","AYNP Code","Product Upload Code","YouTube Link","Manufacturer","Size1","Quantity1","Size2","Quantity2","Size3","Quantity3","Size4","Quantity4"]
            obj.writerow(l)

    if os.path.exists(prof):
        break
    else:
        with open(prof,"w") as a:
            obj = csv.writer(a)
            l = ["Category", "Subcategory", "Name", "Colour", "Weight", "Brand Name", "Vendor Name","Pickup Location","Return Duration","Total Cost","MRP", "Price on Other websites", "Company Discount","Agent Discount", "Profit Margin", "Agent Comission", "YouTube Link", "Size1", "Quantity1", "Size2", "Quantity2", "Size3", "Quantity3", "Size4", "Quantity4"]
            obj.writerow(l)

    if os.path.exists(catf):
        break
    else:
        with open(catf,"w") as a:
            obj = csv.writer(a)
            l=["Category","Subcategory","Code"]
            obj.writerow(l)

def b1():
    win = Tk()
    win.geometry("300x250")
    win.title("ADD Product")
    win.configure(bg="light green")

    def exit1():
        rname = ename.get()
        radd = eadd.get()
        rgst = egst.get()

        with open("Vendor Details.csv", "a", newline="") as file2:
            obj = csv.writer(file2)
            l = [rname.title(), radd, rgst]
            obj.writerow(l)
        win.destroy()

    def save():
        rname = ename.get()
        radd = eadd.get()
        rgst = egst.get()

        with open("Vendor Details.csv", "a", newline="") as file2:
            obj = csv.writer(file2)
            l = [rname.title(), radd, rgst]
            obj.writerow(l)
            ename.delete(0, END)
            eadd.delete(0, END)
            egst.delete(0, END)

    name = Label(win, text="Vendor Name", bg="light green", font=("ariel", 13))
    name.place(x=20, y=20)
    ename = Entry(win)
    ename.place(x=150, y=20)

    add = Label(win, text="Vendor Address", bg="light green", font=("ariel", 13))
    add.place(x=20, y=60)
    eadd = Entry(win)
    eadd.place(x=150, y=60)

    gst = Label(win, text="GST Number", bg="light green", font=("ariel", 13))
    gst.place(x=20, y=100)
    egst = Entry(win)
    egst.place(x=150, y=100)

    # buttons
    sav = Button(win, text="Save \n Add Vendor ", bg="orange", font=("ariel", 13), command=save)
    sav.place(x=40, y=170)

    sae = Button(win, text="Save \n Exit", bg="red", font=("ariel", 13), command=exit1)
    sae.place(x=180, y=170)

def b2():
    win = Tk()
    win.geometry("750x550")
    win.title("ADD Product")
    win.configure(bg="sky blue")

    with open("Manufacturer.csv", "r") as mantab:
        obj = csv.reader(mantab)
        manl = []
        for row in obj:
            if len(row) > 0:
                manl.append(row[0])
            else:
                continue
        manl.remove('Manufacturer Name')


    with open("Category Details.csv", "r") as fcat:
        catobj = csv.reader(fcat)
        catlist = []
        for row in catobj:
            if len(row)>0:
                if row[0] in catlist:
                    continue
                else:
                    catlist.append(row[0])
            else:
                continue
        catlist.remove('Category')


    with open("Vendor Details.csv", "r") as fvend:
        vendobj = csv.reader(fvend)
        vend = []
        for row in vendobj:
            if len(row)>0:
                if row[0] in vend:
                    continue
                else:
                    vend.append(row[0])
            else:
                continue
        vend.remove('Vendor Name')

    def add_size():
        global n, vc, cc, labels, size_list, ply
        rsize = esize.get()
        rq = eq.get()

        size_list.append(rsize)
        size_list.append(rq)

        label = Label(win, text=f"Size: {rsize}, Quantity: {rq}", bg="sky blue", font=("ariel", 12))
        label.place(x=550, y=ply)
        labels.append(label)
        ply += 20

        esize.delete(0, END)
        eq.delete(0, END)

    def sv_exit():
        global n, vc, cc, labels, size_list, ply
        rcat = ecat.get()
        rsub = esub.get()
        rname = ename.get()
        rvname = evname.get()
        riname = einame.get()
        ric = eic.get()
        rcp = float(ecp.get())
        rgst = float(egst.get())
        rpac = float(epac.get())
        rtc = float(etc.get())
        rmrp = float(emrp.get())
        rdsp = float(edsp.get())
        ridsp = float(eidsp.get())
        rweb = float(eweb.get())
        rcd = float(ecd.get())
        rad = float(ead.get())
        rpm = float(epm.get())
        ragc = float(eagc.get())
        raynp = eaynp.get()
        rwc = ewc.get()
        ryc = eyc.get()
        rc = ec.get()
        rb = ebrand.get()
        rweight = eweigh.get()
        rpick = epick.get()
        rrd = erd.get()
        rman = eman.get()

        list1 = [rcat, rsub, rname, rc, rweight, rb, rvname, riname, ric, rpick, rrd, rcp, rgst, rpac, rtc, rmrp, rdsp,ridsp, rweb, rcd, rad, rpm, ragc,raynp, rwc, ryc, rman]
        list2 = [rcat, rsub, rname, rc, rtc, rmrp, rweb, rcd, rad, rpm]
        for i in size_list:
            list1.append(i)
            list2.append(i)

        file1 = open("All Product Details.csv", "a", newline="")
        o1 = csv.writer(file1)
        o1.writerow(list1)

        file2 = open("Product Details.csv", "a", newline="")
        o2 = csv.writer(file2)
        o2.writerow(list2)

        for label in labels:
            label.destroy()
        labels.clear()
        size_list.clear()
        ply = 250

        ecat.delete(0, END)
        esub.delete(0, END)
        ename.delete(0, END)
        evname.delete(0, END)
        einame.delete(0, END)
        eic.delete(0, END)
        ecp.delete(0, END)
        egst.delete(0, END)
        epac.delete(0, END)
        etc.delete(0, END)
        emrp.delete(0, END)
        edsp.delete(0, END)
        eidsp.delete(0, END)
        eweb.delete(0, END)
        ecd.delete(0, END)
        ead.delete(0, END)
        epm.delete(0, END)
        eagc.delete(0, END)
        eaynp.delete(0, END)
        ewc.delete(0, END)
        eyc.delete(0, END)
        ec.delete(0, END)
        epick.delete(0, END)
        ebrand.delete(0, END)
        erd.delete(0, END)
        eweigh.delete(0, END)
        eman.delete(0, END)
        win.destroy()

    def add_product():
        global n, vc, cc, labels, size_list, ply
        rcat = ecat.get()
        rsub = esub.get()
        rname = ename.get()
        rvname = evname.get()
        riname = einame.get()
        ric = eic.get()
        rcp = float(ecp.get())
        rgst = float(egst.get())
        rpac = float(epac.get())
        rtc = float(etc.get())
        rmrp = float(emrp.get())
        rdsp = float(edsp.get())
        ridsp = float(eidsp.get())
        rweb = float(eweb.get())
        rcd = float(ecd.get())
        rad = float(ead.get())
        rpm = float(epm.get())
        ragc = float(eagc.get())
        raynp = eaynp.get()
        rwc = ewc.get()
        ryc = eyc.get()
        rc = ec.get()
        rb = ebrand.get()
        rweight = eweigh.get()
        rpick = epick.get()
        rrd = erd.get()
        rman = eman.get()

        list1 = [rcat, rsub, rname, rc, rweight, rb, rvname, riname, ric, rpick, rrd, rcp, rgst, rpac, rtc, rmrp, rdsp,ridsp, rweb, rcd, rad, rpm, ragc, raynp, rwc, ryc, rman]
        list2 = [rcat, rsub, rname, rc, rtc, rmrp, rweb, rcd, rad, rpm]
        for i in size_list:
            list1.append(i)
            list2.append(i)

        file1 = open("All Product Details.csv", "a", newline="")
        o1 = csv.writer(file1)
        o1.writerow(list1)

        file2 = open("Product Details.csv", "a", newline="")
        o2 = csv.writer(file2)
        o2.writerow(list2)

        for label in labels:
            label.destroy()
        labels.clear()
        size_list.clear()
        ply = 250

        ecat.delete(0, END)
        esub.delete(0, END)
        ename.delete(0, END)
        evname.delete(0, END)
        einame.delete(0, END)
        eic.delete(0, END)
        ecp.delete(0, END)
        egst.delete(0, END)
        epac.delete(0, END)
        etc.delete(0, END)
        emrp.delete(0, END)
        edsp.delete(0, END)
        eidsp.delete(0, END)
        eweb.delete(0, END)
        ecd.delete(0, END)
        ead.delete(0, END)
        epm.delete(0, END)
        eagc.delete(0, END)
        eaynp.delete(0, END)
        ewc.delete(0, END)
        eyc.delete(0, END)
        ec.delete(0, END)
        epick.delete(0, END)
        ebrand.delete(0, END)
        erd.delete(0, END)
        eweigh.delete(0, END)
        eman.delete(0,END)

    def add_colour():
        global n, vc, cc, labels, size_list, ply
        rcat = ecat.get()
        rsub = esub.get()
        rname = ename.get()
        rvname = evname.get()
        riname = einame.get()
        ric = eic.get()
        rcp = float(ecp.get())
        rgst = float(egst.get())
        rpac = float(epac.get())
        rtc = float(etc.get())
        rmrp = float(emrp.get())
        rdsp = float(edsp.get())
        ridsp = float(eidsp.get())
        rweb = float(eweb.get())
        rcd = float(ecd.get())
        rad = float(ead.get())
        rpm = float(epm.get())
        ragc = float(eagc.get())
        raynp = eaynp.get()
        rwc = ewc.get()
        ryc = eyc.get()
        rc = ec.get()
        rb = ebrand.get()
        rweight = eweigh.get()
        rpick = epick.get()
        rrd = erd.get()
        rman = eman.get()

        list1 = [rcat, rsub, rname, rc, rweight, rb, rvname, riname, ric, rpick, rrd, rcp, rgst, rpac, rtc, rmrp, rdsp,
                 ridsp, rweb, rcd, rad, rpm, ragc,
                 raynp, rwc, ryc, rman]
        list2 = [rcat, rsub, rname, rc, rtc, rmrp, rweb, rcd, rad, rpm]
        for i in size_list:
            list1.append(i)
            list2.append(i)

        file1 = open("All Product Details.csv", "a", newline="")
        o1 = csv.writer(file1)
        o1.writerow(list1)

        file2 = open("Product Details.csv", "a", newline="")
        o2 = csv.writer(file2)
        o2.writerow(list2)

        for label in labels:
            label.destroy()
        labels.clear()
        size_list.clear()
        ply = 250

        ecp.delete(0, END)
        egst.delete(0, END)
        epac.delete(0, END)
        etc.delete(0, END)
        emrp.delete(0, END)
        edsp.delete(0, END)
        eidsp.delete(0, END)
        eweb.delete(0, END)
        ecd.delete(0, END)
        ead.delete(0, END)
        epm.delete(0, END)
        eagc.delete(0, END)
        eaynp.delete(0, END)
        ewc.delete(0, END)
        eyc.delete(0, END)
        ec.delete(0, END)


    def generate():
        global n, vc, cc, labels, size_list, ply
        with open("All Product Details.csv", "r") as file1:
            red = csv.reader(file1)
            for i in red:
                if len(i)>0:
                    if len(str(n)) == 1:
                        ay = cc + vc + "00" + str(n)
                    elif len(str(n)) == 2:
                        ay = cc + vc + "0" + str(n)
                    else:
                        ay = cc + vc + str(n)
                    if ay == i[23]:
                        n += 1
                    else:
                        continue

        p = int(ecp.get())
        g = int(egst.get())
        rpac = int(epac.get())
        rtc = int(p + (p * (g / 100)) + rpac)
        rmrp = rtc * 3
        rdsp = int(rtc + (rtc * 0.51))
        ridsp = int(rtc + (rtc * 0.40))
        rweb = rdsp + 150
        rcd = rmrp - rdsp
        rad = rdsp - ridsp
        rpm = rmrp - rtc
        ragc = (ridsp - rtc) // 3

        etc.delete(0, END)
        emrp.delete(0, END)
        edsp.delete(0, END)
        eidsp.delete(0, END)
        eweb.delete(0, END)
        ecd.delete(0, END)
        ead.delete(0, END)
        epm.delete(0, END)
        eagc.delete(0, END)
        eaynp.delete(0, END)

        eaynp.insert(0, ay)
        etc.insert(0, rtc)
        emrp.insert(0, rmrp)
        edsp.insert(0, rdsp)
        eidsp.insert(0, ridsp)
        eweb.insert(0, rweb)
        ecd.insert(0, rcd)
        ead.insert(0, rad)
        epm.insert(0, rpm)
        eagc.insert(0, ragc)

    def cls():
        global n, vc, cc, labels, size_list, ply
        a=labels.pop()
        a.destroy()
        size_list.pop()
        ply = 250

    def update_esub(event):
        global n, vc, cc, labels, size_list, ply
        esub.delete(0, END)
        with open("Category Details.csv", "r") as fcat:
            catobj = csv.reader(fcat)
            got = ecat.get()
            z = []
            for i in catobj:
                if len(i)>0:
                    if got == i[0]:
                        z.append(i[1])
                else:
                    continue

            esub["values"] = (z)

    def update_code(event):
        global n, vc, cc, labels, size_list, ply
        with open("Category Details.csv", "r") as fcat:
            catobj = csv.reader(fcat)
            got = ecat.get()
            subgot = esub.get()
            for i in catobj:
                if len(i)>0:
                    if got == i[0] and subgot == i[1]:
                        cc = i[2]
                else:
                    continue

    def update_vc(event):
        global n, vc, cc, labels, size_list, ply
        rman = eman.get()
        with open("Manufacturer.csv", "r") as fvend:
            vendobj = csv.reader(fvend)
            for i in vendobj:
                if len(i)>0:
                    if rman == i[0]:
                        vc = i[1]
                else:
                    continue
    
    # def search(event):
        

    # 1st row
    cat = Label(win, text="Category", bg="sky blue", font=("ariel", 12))
    cat.place(x=20, y=20)
    ecat = ttk.Combobox(win)
    ecat['values'] = (catlist)
    ecat.place(x=100, y=20)
    ecat.bind("<<ComboboxSelected>>", update_esub)

    sub = Label(win, text="Sub Category", bg="sky blue", font=("ariel", 12))
    sub.place(x=265, y=20)
    esub = ttk.Combobox(win, width=15)
    esub.place(x=370, y=20)
    esub.bind("<<ComboboxSelected>>", update_code)

    brand = Label(win, text="Brand Name", bg="sky blue", font=("ariel", 12))
    brand.place(x=500, y=20)
    ebrand = Entry(win)
    ebrand.place(x=600, y=20)

    # 2nd row
    name = Label(win, text="Product Name", bg="sky blue", font=("ariel", 12))
    name.place(x=20, y=50)
    ename = Entry(win)
    ename.place(x=135, y=50)

    vname = Label(win, text="Vendor Name", bg="sky blue", font=("ariel", 12))
    vname.place(x=270, y=50)

    evname = ttk.Combobox(win)
    evname["values"] = (vend)
    evname.place(x=380, y=50)
    evname.bind("<<ComboboxSelected>>", update_vc)

    weigh = Label(win, text="Weight", bg="sky blue", font=("ariel", 12))
    weigh.place(x=530, y=50)
    eweigh = Entry(win)
    eweigh.place(x=600, y=50)

    # 3rd Row
    iname = Label(win, text="Item Name", bg="sky blue", font=("ariel", 12))
    iname.place(x=20, y=80)

    einame = Entry(win)
    einame.place(x=105, y=80)

    ic = Label(win, text="Item Code", bg="sky blue", font=("ariel", 12))
    ic.place(x=260, y=80)

    eic = Entry(win)
    eic.place(x=360, y=80)

    c = Label(win, text="Colour", bg="sky blue", font=("ariel", 12))
    c.place(x=505, y=80)
    ec = Entry(win)
    ec.place(x=570, y=80)

    ######

    man = Label(win, text="Manufacturer Name", bg="sky blue", font=("ariel", 12))
    man.place(x=20, y=110)
    eman = ttk.Combobox(win)
    eman["values"] = (manl)
    eman.place(x=170, y=110)
    eman.bind("<<ComboboxSelected>>", update_vc)

    # 4th Row
    cp = Label(win, text="Cost Price", bg="sky blue", font=("ariel", 12))
    cp.place(x=20, y=150)
    ecp = Entry(win, width=15)
    ecp.place(x=105, y=150)

    gst = Label(win, text="GST(%)", bg="sky blue", font=("ariel", 12))
    gst.place(x=210, y=150)
    egst = Entry(win, width=10)
    egst.place(x=280, y=150)

    pac = Label(win, text="Packing", bg="sky blue", font=("ariel", 12))
    pac.place(x=360, y=150)
    epac = Entry(win, width=10)
    epac.place(x=430, y=150)

    size = Label(win, text="Size", bg="sky blue", font=("ariel", 12))
    size.place(x=510, y=150)
    esize = Entry(win)
    esize.place(x=570, y=150)

    # 5th Row
    pick = Label(win, text="Pickup Location", bg="sky blue", font=("ariel", 12))
    pick.place(x=20, y=180)
    epick = Entry(win, width=50)
    epick.place(x=150, y=180)

    q = Label(win, text="Quantity", bg="sky blue", font=("ariel", 12))
    q.place(x=500, y=180)
    eq = Entry(win)
    eq.place(x=570, y=180)

    # 6th row
    tc = Label(win, text="Total Cost", bg="sky blue", font=("ariel", 12))
    tc.place(x=20, y=210)
    etc = Entry(win)
    etc.place(x=110, y=210)

    rd = Label(win, text="Return Duration (Days)", bg="sky blue", font=("ariel", 12))
    rd.place(x=250, y=210)
    erd = Entry(win)
    erd.place(x=430, y=210)

    btn = Button(win, text="Add size", bg="peach puff", font=("ariel", 14, "bold"), command=add_size)
    btn.place(x=580, y=210)

    # 7th row
    mrp = Label(win, text="MRP", bg="sky blue", font=("ariel", 12))
    mrp.place(x=20, y=240)

    emrp = Entry(win, width=15)
    emrp.place(x=70, y=240)

    dsp = Label(win, text="Direct Selling Price", bg="sky blue", font=("ariel", 12))
    dsp.place(x=200, y=240)

    edsp = Entry(win)
    edsp.place(x=350, y=240)

    # 8th row
    idsp = Label(win, text="Indirect Selling Price", bg="sky blue", font=("ariel", 12))
    idsp.place(x=20, y=270)

    eidsp = Entry(win, width=13)
    eidsp.place(x=170, y=270)

    web = Label(win, text="Other Website Price", bg="sky blue", font=("ariel", 12))
    web.place(x=270, y=270)

    eweb = Entry(win, width=13)
    eweb.place(x=420, y=270)

    # 9th Row
    cd = Label(win, text="Company Discount", bg="sky blue", font=("ariel", 12))
    cd.place(x=20, y=300)

    ecd = Entry(win, width=13)
    ecd.place(x=170, y=300)

    ad = Label(win, text="Agent Discount", bg="sky blue", font=("ariel", 12))
    ad.place(x=280, y=300)

    ead = Entry(win, width=13)
    ead.place(x=400, y=300)

    # 10th Row
    pm = Label(win, text="Profit Margin", bg="sky blue", font=("ariel", 12))
    pm.place(x=20, y=330)

    epm = Entry(win)
    epm.place(x=120, y=330)

    agc = Label(win, text="Agent Commission", bg="sky blue", font=("ariel", 12))
    agc.place(x=250, y=330)

    eagc = Entry(win)
    eagc.place(x=400, y=330)

    # 11th Row
    aynp = Label(win, text="AYNP Code", bg="sky blue", font=("ariel", 12))
    aynp.place(x=20, y=360)

    eaynp = Entry(win)
    eaynp.place(x=120, y=360)

    wc = Label(win, text="Website Code", bg="sky blue", font=("ariel", 12))
    wc.place(x=270, y=360)

    ewc = Entry(win)
    ewc.place(x=390, y=360)

    # 12 Row
    yc = Label(win, text="YouTube Link", bg="sky blue", font=("ariel", 12))
    yc.place(x=20, y=390)

    eyc = Entry(win, width=60)
    eyc.place(x=130, y=390)

    # 13th Row
    gen = Button(win, text="Generate", bg="thistle1", font=("ariel", 14), command=generate)
    gen.place(x=350, y=425)

    # 14th Row
    sc = Button(win, text="Save \n Add Colour", bg="orange", font=("ariel", 14), command=add_colour)
    sc.place(x=40, y=470)

    sp = Button(win, text="Save \n Add Product", bg="lime green", font=("ariel", 14), command=add_product)
    sp.place(x=200, y=470)

    se = Button(win, text="Save \n Exit", bg="red", font=("ariel", 14), command=sv_exit)
    se.place(x=370, y=470)

    search = Button(win, text="Search", bg="chocolate", font=("ariel", 14))
    search.place(x=470, y=470)

    rem = Button(win, text="Clear size", bg="RoyalBlue1", font=("ariel", 14), command=cls)
    rem.place(x=580, y=470)

def b3():
    win = Tk()
    win.geometry("300x250")
    win.title("ADD Product")
    win.configure(bg="gold")

    def generate_random_code():
        return ''.join(random.choices(string.ascii_uppercase, k=3))

    def insert_code():
        rcat = ecat.get()
        rsubcat = esubcat.get()
        if rcat and rsubcat:
            random_code = generate_random_code()
            be = random_code.upper()
            ecode.delete(0, END)
            ecode.insert(0, be)

    def exit1():
        rcat = ecat.get()
        rsubcat = esubcat.get()
        rcode = ecode.get()
        code_taken = False

        with open("Category Details.csv", "r") as file1:
            red = csv.reader(file1)
            for row in red:
                if len(row) > 0:
                    if rcode == row[1]:
                        code_taken = True
                        break
                else:
                    continue

        if code_taken:
            tkinter.messagebox.showinfo("Code Taken", "Enter New Code")
            ecode.delete(0, END)
        else:
            with open("Category Details.csv", "a", newline="") as file2:
                obj = csv.writer(file2)
                l = [rcat.title(), rsubcat.title(), rcode]
                obj.writerow(l)
            win.destroy()

    def save():
        rcat = ecat.get()
        rsubcat = esubcat.get()
        rcode = ecode.get()
        code_taken = False

        with open("Category Details.csv", "r") as file1:
            red = csv.reader(file1)
            for row in red:
                if len(row) > 0:
                    if rcode == row[1]:
                        code_taken = True
                        break
                else:
                    continue

        if code_taken:
            tkinter.messagebox.showinfo("Code Taken", "Enter New Code")
            ecode.delete(0, END)
        else:
            with open("Category Details.csv", "a", newline="") as file2:
                obj = csv.writer(file2)
                l = [rcat.title(), rsubcat.title(), rcode]
                obj.writerow(l)
                ecat.delete(0, END)
                esubcat.delete(0, END)
                ecode.delete(0, END)

    cat = Label(win, text="Category", bg="gold", font=("ariel", 13))
    cat.place(x=20, y=20)
    ecat = Entry(win, width=25)
    ecat.place(x=130, y=20)

    subcat = Label(win, text="Sub Category", bg="gold", font=("ariel", 13))
    subcat.place(x=20, y=50)
    esubcat = Entry(win, width=25)
    esubcat.place(x=130, y=50)

    code = Label(win, text="Code", bg="gold", font=("ariel", 13))
    code.place(x=50, y=80)
    ecode = Entry(win, width=25)
    ecode.place(x=130, y=80)

    # buttons
    sav = Button(win, text="Save \n Add Category ", bg="Dark orange", font=("ariel", 13), command=save)
    sav.place(x=40, y=180)

    sae = Button(win, text="Save \n Exit", bg="red", font=("ariel", 13), command=exit1)
    sae.place(x=180, y=180)

    gen = Button(win, text="Generate ", bg="White", font=("ariel", 13), command=insert_code)
    gen.place(x=110, y=120)

def b4():
    win = Tk()
    win.geometry("300x250")
    win.title("ADD Manufacturer")
    win.configure(bg="orchid2")

    def generate_random_code():
        return ''.join(random.choices(string.ascii_uppercase, k=3))

    def insert_code():
        rname = ename.get()
        if rname:
            random_code = generate_random_code()
            be = random_code.upper()
            ecode.delete(0, END)
            ecode.insert(0, be)

    def exit1():
        rname = ename.get()
        rcode = ecode.get()
        code_taken = False

        with open("Manufacturer.csv", "r") as file1:
            red = csv.reader(file1)
            for row in red:
                if len(row) > 0:
                    if rcode == row[1]:
                        code_taken = True
                        break
                else:
                    continue

        if code_taken:
            tkinter.messagebox.showinfo("Code Taken", "Enter New Code")
            ecode.delete(0, END)
        else:
            with open("Manufacturer.csv", "a", newline="") as file2:
                obj = csv.writer(file2)
                l = [rname.title(), rcode]
                obj.writerow(l)
            win.destroy()

    def save():
        rname = ename.get()
        rcode = ecode.get()
        code_taken = False

        with open("Manufacturer.csv", "r") as file1:
            red = csv.reader(file1)
            for row in red:
                if len(row)>0:
                    if rcode == row[1]:
                        code_taken = True
                        break
                else:
                    continue

        if code_taken:
            tkinter.messagebox.showinfo("Code Taken", "Enter New Code")
            ecode.delete(0, END)
        else:
            with open("Manufacturer.csv", "a", newline="") as file2:
                obj = csv.writer(file2)
                l = [rname.title(), rcode]
                obj.writerow(l)
                ename.delete(0, END)
                ecode.delete(0, END)

    name = Label(win, text="Manufacturer \n Name", bg="orchid2", font=("ariel", 13))
    name.place(x=20, y=20)
    ename = Entry(win, width=25)
    ename.place(x=130, y=20)

    code = Label(win, text="Code", bg="orchid2", font=("ariel", 13))
    code.place(x=50, y=70)
    ecode = Entry(win, width=25)
    ecode.place(x=130, y=70)

    # buttons
    sav = Button(win, text="Save \n Add Manufacturer ", bg="Dark orange", font=("ariel", 13), command=save)
    sav.place(x=30, y=170)

    sae = Button(win, text="Save \n Exit", bg="red", font=("ariel", 13), command=exit1)
    sae.place(x=210, y=170)

    gen = Button(win, text="Generate ", bg="White", font=("ariel", 13), command=insert_code)
    gen.place(x=110, y=120)


btn1 = Button(root, text = "ADD Vendor", bg = "white", relief = "raised", font = ("ariel",15,"bold"),command=b1)
btn1.place(x=35, y=220)

btn2 = Button(root, text = "ADD Product", bg = "white", relief = "raised", font = ("ariel",15,"bold"),command=b2)
btn2.place(x=30, y=300)

btn3 = Button(root, text = "ADD Category", bg = "white", relief = "raised", font = ("ariel",15,"bold"),command=b3)
btn3.place(x=210, y=300)

btn4 = Button(root, text = "ADD Manufacturer", bg = "white", relief = "raised", font = ("ariel",15,"bold"),command=b4)
btn4.place(x=190, y=220)
root.mainloop()
# -*- coding: utf-8 -*-
#Chucky_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile,wikipedia

cl = LINETCR.LINE()
cl.login(token='EpVJyuttJI1xnBaeW22e.4XYCC3ch5Y6UL7gxKHdrhG.4ejKIpAElhmbzwqQFqad+faosnUKzmnMOudpYFgmXDk=')
cl.loginResult()
print "Cl-Login Success\n"

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔═════════════
║ NvStar Public
╠═════════════
║ PUBLIC COMMAND 
╠═════════════
║╔════════════
║╠❂➣ /me
║╠❂➣ /mymid
║╠❂➣ /gcreator
║╠❂➣ /ginfo
║╠❂➣ /memberlist
║╠❂➣ /Searchid: 「Text」
║╠❂➣ /checkdate 「DD-MM-YYYY」
║╠❂➣ /kalender
║╠❂➣ /creator
║╠❂➣ /playstore 「namaAPP」
║╠❂➣ /musik 「judul-penyanyi」
║╠❂➣ /lirik 「judil-penyanyi」
║╠❂➣ /ig 「username」 
║╠❂➣ wikipedia 「text」
║╠❂➣ pp @
║╠❂➣ cover @
║╠❂➣ getbio @
║╠❂➣ getinfo @
║╠❂➣ getname @
║╠❂➣ Set ➣ Check
║╠❂➣ Speed
║╠❂➣ Tagall 
║╠❂➣ Apakah
║╠❂➣ Kapan
║╠❂➣ Hari
║╠❂➣ Berapa
║╠❂➣ Berapakah
║╠❂➣ Translate
║╠❂➣ /bye-bye
║╚════════════
╠═════════════
║ Ketik commandnya
║ Harus sesuai yaa kak
║ (/*’-‘*)/
╚═════════════
"""

nvstar="ua5f2cbc325816777be5ef529eb920c50"

helpTranslate ="""
╔═════════════
║ NvStar Public
╠═════════════
║ TRANSLATE 
╠═════════════
║╔════════════
║╠❂➣ Id@en
║╠❂➣ En@id
║╠❂➣ Id@jp
║╠❂➣ Jp@id
║╠❂➣ Id@th
║╠❂➣ Th@id
║╠❂➣ Id@ar
║╠❂➣ Ar@id
║╠❂➣ Id@ko
║╠❂➣ Ko@id
║╚════════════
╠═════════════
║ Ketik commandnya
║ Harus sesuai yaa kak
║ (/*’-‘*)/
╚═════════════
"""

helpCreator ="""
╔═════════════
║ NvStar Public
╠═════════════
║ TRANSLATE 
╠═════════════
║╔════════════
║╠❂➣ Runtime
║╠❂➣ Bc: 「text」
║╠❂➣ Glist
║╠❂➣ Group id
║╠❂➣ Removechat
║╠❂➣ Reboot
║╠❂➣ Friendlist
║╚════════════
╠═════════════
║ Ketik commandnya
║ Harus sesuai yaa kak
║ (/*’-‘*)/
╚═════════════
"""


KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
Creator=["ua5f2cbc325816777be5ef529eb920c50"]
admin=["ua5f2cbc325816777be5ef529eb920c50"]


contact = cl.getProfile()
backup1 = cl.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = cl.getProfile().displayName


wait = {
    "AutoJoinCancel":True,
    "memberscancel":1,
    "Members":1,
    'detectMention':True,
    "Sambutan":True,
    "alwaysRead":True,  	
    "lang":"JP",
}


cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items


def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      


def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False  


def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e


def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True


def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)


def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e


def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              cl.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                cl.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Nah lhoo~ " + " " + nick[0] + " " + "\nNgintip Aja Niih. . .\nChat dulu sana sama yang lain   ")
                                    else:
                                        cl.sendText(op.param1, "Hayoo " + " " + nick[1] + " " + "\nChat bareng sini, baru buka HPnya kan   ")
                                else:
                                    cl.sendText(op.param1, "Ngintip~? " + " " + Name + " " + "\nBaru buka groupnya yaa, chat dulu sonoh")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)

        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)

	    if mid in op.param3:
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"" + cl.getContact(op.param2).displayName + "\nMaav kaka... Membernya kurang dari 10 Orang.\nInvite aku lagi yahh kalo sudah lebih dari 10 orang\n\n༼ つ ಥ_ಥ ༽つ")
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"Haloo kaka - kaka semua.\nSilahkan ketik 「Help」 untuk melihat command list.\nPakai dengan bijak yaahh (づ｡◕‿‿◕｡)づ")

        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo.. " + cl.getContact(op.param2).displayName + "\nSelamat datang di " + str(ginfo.name) + "\nSemoga betah yaa disini\n\n(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            cl.sendText(op.param1,"Yahhh kaka kok pergi sih " + cl.getContact(op.param2).displayName + "\nAku kangen kamu kak (ू˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ू)")
            print "MEMBER HAS LEFT THE GROUP"

        if op.type == 26:
            msg = op.message

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Hallo kaka o(≧∇≦o)","˭̡̞(◞⁎˃ᆺ˂)◞*✰ " + cName + " Ada apa kaka?",cName + " Aku lagi males di tag kak (╬ﾟ◥益◤ﾟ) ╬ﾟ","(*⌒▽⌒*)θ～♪ ", cName + " Ketik 「Help」 yaa kak", "Kenapa kak ｢(ﾟ<ﾟ)ﾞ?? " + cName, "Hallo kak " + cName + "Aku ngantuk nih (●´ω｀●)ゞ","KABURRR~~! kaka" + cName + "Genit panggil² Aku\nε=ε=ε=ε=ε” “(/*’-‘*)/"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break                               

#===========Help Key Start===========
            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)
				
            elif msg.text in ["Translate"]:
                cl.sendText(msg.to,helpTranslate)
				
            elif msg.text in ["Help creator"]:
                cl.sendText(msg.to,helpCreator)
#===========Help Key Finish==========


#======================================================================PUBLIC COMMAND======================================================================


#===========Me Start============
            elif msg.text.lower() in ["/me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
#===========Me Finish===========


#===========Mymid Start============
            elif msg.text.lower() in ["/mymid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                kr.sendText(msg.to,middd)
#===========Mymid Finish===========


#===========gcreator Start=============
	    elif msg.text in ["/gcreator"]:
		ginfo = nadya.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                nadya.sendMessage(msg)
		nadya.sendText(msg.to,"Tuhh kak yang buat group ini\n.+:｡(ﾉ･ω･)ﾉﾞ")
#===========gcreator Finish============


#===========ginfo start=============
            elif msg.text == "/ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Nama group]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[Nama group]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
#===========ginfo finish============


#===========member list start=============
            elif msg.text in ["/memberlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="[LIST MEMBER]"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n[LIST MEMBER]\n\nTotal Membernya ada : %i kak \nΣ(*ﾉ´>ω<｡`)ﾉ" % len(group)
                cl.sendText(msg.to, msgs)
#===========member list finish============


#===========searchid start=============
            elif "/searchid: " in msg.text:
                userid = msg.text.replace("/searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg) 
#===========searchid finish============


#===========Checkdate start==============
            elif "/checkdate " in msg.text:
                tanggal = msg.text.replace("/checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Ini kak informasi tanggal lahirnya\n\n"+"Tanggal lahir : "+lahir+"\nUmur : "+usia+"\nUlang tahun : "+ultah+"\nZodiak : "+zodiak+"\n(((o(*ﾟ▽ﾟ*)o)))")
#===========Checkdate finish=============


#===========Kalender start===============
            elif msg.text in ["/kalender"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst ="Kaka tanya kalender?\nSekarang Hari " + hasil + "" + inihari.strftime('%d') + " Bulan " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst) 
#===========Kalender Finish==============


#===========Pp @ start================
            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Nggak ketemu kak (๑◕︵◕๑)\nMungkin nama doi pakai unicode")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload gambar profile si doi gagal kak\n(๑◕︵◕๑)")

            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Nggak ketemu kak (๑◕︵◕๑)\nMungkin nama doi pakai unicode")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload gambar profile si doi gagal kak\n(๑◕︵◕๑)")
#===========Pp @ finish===============


#===========cover @ start=================
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Nggak ketemu kak (๑◕︵◕๑)\nMungkin nama doi pakai unicode")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload gambar cover si doi gagal kak\n(๑◕︵◕๑)")
								
            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Nggak ketemu kak (๑◕︵◕๑)\nMungkin nama doi pakai unicode")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload gambar cover si doi gagal kak\n(๑◕︵◕๑)")
#===========cover @ finish================


#===========getbio @ Start==================
            elif "getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "Ini kak bionya （＊〇□〇）……！\n\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "Ini kak bionya （＊〇□〇）……！\n\n" + contact.statusMessage)
#===========getbio @ Finish=================


#===========getinfo @ Start===================
            elif "getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid Maav kak nomor MIDnya si doi harus ketik 「/mymid」 :\n" + "\n\nBio :\n" + contact.statusMessage + "\n\nGambar Profile :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\nMaav kak nomor MIDnya si doi harus ketik 「/mymid」 " + "\n\nBio :\n" + contact.statusMessage + "\n\nGambar Profile :\n" + str(cu))
#===========getinfo @ Finish==================


#===========getname @ Start===================
            elif "getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "Ini kak nama copy'an si doi\n°˖✧◝(⁰▿⁰)◜✧˖°\n\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "Ini kak nama copy'an si doi\n°˖✧◝(⁰▿⁰)◜✧˖°\n\n" + contact.displayName)
#===========getname @ Finish===================


#===========creator Start====================
            elif msg.text in ["/creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': nvstar}
		cl.sendText(msg.to,"Hallo kak ini contact orang yang buat aku\n೭੧(❛▿❛✿)੭೨")
                cl.sendMessage(msg)
#===========creator Finish===================


#===========playstore Start=====================
            elif "Playstore " in msg.text.lower():
                tob = msg.text.lower().replace("Playstore ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"Nama App : "+tob+"\nSumber : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                cl.sendText(msg.to,"Ituu~ kak link appnya.\no(〃＾▽＾〃)o")
#===========playstore Finish====================


#===========musik Start=====================
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Judul : " + song[0] + "\nDurasi : " + song[1] + "\nLink download : " + song[4] + "\n\nSebentar yaa kak lagunya ku proses dulu")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Sudah selsai kak lagu " + song[0] + " Bisa langsung di play musiknya\n\n(◦′ᆺ‵◦)♬°✧❥✧¸.•*¨*✧♡✧ℒℴѵℯ✧♡✧*¨*•.❥")
#===========musik Finish===================


#===========lirik Start===================
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#===========lirik Finish===================


#===========Ig Start===================
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "(╭☞´ิ∀´ิ)╭☞ Ini kak Instagramnya\n"
                    details = ""
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#===========Ig Finish===================


#===========wikipedia Start===================
            elif 'Wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Judul ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Maav kak... Textnya terlalu banyak\n(っ◞‸◟c)\n\nKlik link dibawah ini kak untuk membacanya\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#===========wikipedia Finish==================


#===========Set > Check Start==================
            elif msg.text in ["Setview","Setpoint","Cctv","Set"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Ketik 「Check」 lihat yang ngintip kak\n!(•̀ᴗ•́)و ̑̑")
                print "Setpoint"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║ Ini kak yang ngintip (*ﾟﾛﾟ)\n╠═════════════════════════\n╠❂➣"
                        grp = '\n╠❂➣ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠❂➣ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                    else:
                        cl.sendText(msg.to, "Belum ada yang ngintip kak (•̥́_•ૅू˳)")
                    print "Ceksider"
#===========Set > Check Finish==================


#===========Speed Start==================
            elif msg.text in ["Speedbot"]:
                start = time.time()
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s\nItu kecepatan ku kak (๑˃̵ᴗ˂̵)و" % (elapsed_time))         
#===========Speed Finish=================


#===========Tagall Start=================
            elif msg.text in ["Tagall","Ats"]:
                if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                      cl.sendText(msg.to,"Cilukbaa~~ (≧д≦ヾ)")
                  except Exception as error:
                      print error
#===========Tagall Finish================


#===========Kerang Ajaib Start================
            elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Ya","Tidak","Mungkin","Bacot","Gue capek ditanya terus"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Hari " in msg.text:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                


            elif "Berapa " in msg.text:
                apk = msg.text.replace("Berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Berapakah " in msg.text:
                apk = msg.text.replace("Berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "Kapan " in msg.text:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah","Tidak tau"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#===========Kerang Ajaib Finish===============


#===========KELUAR START============
            elif msg.text in ["/bye-bye"]:
		    cl.sendText(msg.to, "Kaka jahat aku di usir\n˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚")
		    cl.leaveGroup(msg.to)
#===========KELUAR FINISH===========


#======================================================================TRANSLATE COMMAND======================================================================


            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI IDN]==\n" + "" + kata + "\n\n==[KE ENG]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI ENG]==\n" + "" + kata + "\n\n==[KE IDN]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")
                
            
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI IDN]==\n" + "" + kata + "\n\n==[KE JPN]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")
                
            
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI JPN]==\n" + "" + kata + "\n\n==[KE IDN]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")

            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI IDN]==\n" + "" + kata + "\n\n==[KE THA]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")


            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI THA]==\n" + "" + kata + "\n\n==[KE IDN]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")
  

            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI IDN]==\n" + "" + kata + "\n\n==[KE ARG]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")


            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI AR]==\n" + "" + kata + "\n\n==[KE IDN]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")


            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI IDN]==\n" + "" + kata + "\n\n==[KE KOR]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")


            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[DARI KOR]==\n" + "" + kata + "\n\n==[KE IDN]==\n" + "" + result + "\n\nSukses kak\n ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ")
				
#======================================================================CREATOR COMMAND======================================================================


#==========RUNTIME START============
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Aku sudah berjalan selama :\n\n"+waktu(eltime)+"\nItu Kak\n☆ミヾ(∇≦((ヾ(≧∇≦)〃))≧∇)ノ彡☆"
                cl.sendText(msg.to,van)
#==========RUNTIME FINISH===========

#===========BROADCAST START==========
	    elif "Bc " in msg.text:
		bc = msg.text.replace("Bc ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Ada Broadcast dari majikan ku kak\n☆*:.｡.o(≧▽≦)o.｡.:*☆\n\n"+bc+"\n\nContact Me : line.me/ti/p/~KazeReborn")
		    cl.sendText(msg.to,"Broadcast Success")
#===========BROADCAST FINISH=========


#===========GROUP LIST START==========
            elif msg.text in ["Glist"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠❂➣ " + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╔═════════════════════════\n║ Ini kak group listnya ☚(ﾟヮﾟ☚)\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Totalnya =" +" ["+str(len(gid))+"]\n╚═════════════════════════")
#===========GROUP LIST FINISH=========


#===========GROUP ID LIST START============
            elif msg.text in ["Group id"]:
                if msg.from_ in Creator:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)
#===========GROUP ID LIST FINISH===========


#===========FRIEND LIST START===========
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="Ini kak teman teman aku (✿◠‿◠)"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════[FRIEND LIST]═════════\n\nTotalnya : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
#===========FRIEND LIST FINISH==========


#===========REMOVE CHAT START============
            elif "removechat" in msg.text.lower():
                if msg.from_ in Creator:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Chatnya sudah bersih\nd=(´▽｀)=b")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")  
#===========REMOVE CHAT FINISH===========


#===========REBOOOT START===========
	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Sebentar kak robotnya ku restart dulu\n(๑>ᴗ<๑)")
		    restart_program()
		    print "@Restart"
#===========REBOOOT FINISH==========


        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
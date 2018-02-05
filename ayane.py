# -*- coding: utf-8 -*-
#aldierG_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

aldier = LINETCR.LINE()
#aldier.login(qr=True)
#aldier.login(mail='aldiergokil@gmail.com', passwd='mobilku123')
aldier.login(token='EpxIivMO8G4kgbJLzqma.uP7qJPAlQDehEegg62A3AG.XflC9hCnZ4QnjEkS0k5NuAcPkMNXjFGZeTNeQJynj4Y=')
aldier.loginResult()
print "aldier-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ SELF COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Me
║╠❂➣ Mymid
║╠❂➣ Mid @
║╠❂➣ SearchID:
║╠❂➣ Checkdate (DD/MM/YY)
║╠❂➣ Kalender
║╠❂➣ Steal contact 
║╠❂➣ Pp @ 
║╠❂➣ Cover @ 
║╠❂➣ Auto like 
║╠❂➣ Scbc Text 
║╠❂➣ Cbc Text 
║╠❂➣ Gbc Text 
║╠❂➣ Getbio @ 
║╠❂➣ Getinfo @ 
║╠❂➣ Getname @ 
║╠❂➣ Getprofile @ 
║╠❂➣ Getcontact @ 
║╠❂➣ Getvid @ 
║╠❂➣ Friendlist 
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

botMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ BOT COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Absen 
║╠❂➣ Respon 
║╠❂➣ Runtime 
║╠❂➣ Mycopy @
║╠❂➣ Mybackup
║╠❂➣ Mybio
║╠❂➣ @bye
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

mediaMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ MEDIA COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Gift 
║╠❂➣ Gift1 @ s/d Gift10 @ 
║╠❂➣ Giftbycontact 
║╠❂➣ All gift 
║╠❂➣ Google: 
║╠❂➣ Playstore [NamaApp] 
║╠❂➣ Fancytext: Text 
║╠❂➣ /musik [Judul-Penyanyi]
║╠❂➣ /lirik [Judul-Penyanyi]
║╠❂➣ /musrik [Judul-Penyanyi]
║╠❂➣ /ig [Ursname] 
║╠❂➣ Checkig [Ursname] 
║╠❂➣ Apakah 
║╠❂➣ Kapan
║╠❂➣ Hari
║╠❂➣ Berapa
║╠❂➣ Berapakah 
║╠❂➣ wikipedia [text]
║╠❂➣ /Youtubelink: 
║╠❂➣ /Youtubevideo:
║╠❂➣ /Youtubesearch:
║╠❂➣ Image NamaGambar 
║╠❂➣ Say-id 
║╠❂➣ Say-en 
║╠❂➣ Say-jp 
║╠❂➣ Image
║╠❂➣ Tr-id
║╠❂➣ Tr-en
║╠❂➣ Id@en
║╠❂➣ En@id
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

groupMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ GROUP COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Welcome
║╠❂➣ Invite creator 
║╠❂➣ Setview
║╠❂➣ Viewseen
║╠❂➣ Gn: (NamaGroup) 
║╠❂➣ Tag all 
║╠❂➣ Recover 
║╠❂➣ Cancel 
║╠❂➣ Cancelall 
║╠❂➣ Gcreator 
║╠❂➣ Ginfo 
║╠❂➣ Gurl 
║╠❂➣ Glist
║╠❂➣ Pict group: (NamaGroup) 
║╠❂➣ Spam: (Text) 
║╠❂➣ Add all 
║╠❂➣ Kick: (Mid) 
║╠❂➣ Invite: (Mid) 
║╠❂➣ Invite 
║╠❂➣ Memlist 
║╠❂➣ Getgroup image 
║╠❂➣ Urlgroup Image 
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""
WIB="u529ed08e968ba9d107784186eb66b76a"

setMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ SET COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Sambutan on/off 
║╠❂➣ Url on/off 
║╠❂➣ Alwaysread on/off 
║╠❂➣ Sider on/off 
║╠❂➣ Contact on/off 
║╠❂➣ Simisimi on/off 
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

creatorMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ CREATOR COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Admin add @ 
║╠❂➣ Admin remove @ 
║╠❂➣ Bc: (Text) 
║╠❂➣ Join group: (NamaGroup)
║╠❂➣ Leave group: (NamaGroup)
║╠❂➣ Leave all group 
║╠❂➣ Tag on/off 
║╠❂➣ Bot restart 
║╠❂➣ Turn off 
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

adminMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ ADMIN COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Admin list 
║╠❂➣ Allprotect on/off 
║╠❂➣ Ban 
║╠❂➣ Unban 
║╠❂➣ Ban @ 
║╠❂➣ Unban @ 
║╠❂➣ Ban list 
║╠❂➣ Clear ban 
║╠❂➣ Kill 
║╠❂➣ Kick @ 
║╠❂➣ Set member: (Jumblah) 
║╠❂➣ Ban group: (NamaGroup)
║╠❂➣ Del ban: (NamaGroup)
║╠❂➣ List ban 
║╠❂➣ Kill ban 
║╠❂➣ Glist 
║╠❂➣ Glistmid 
║╠❂➣ Details group: (Gid) 
║╠❂➣ Cancel invite: (Gid) 
║╠❂➣ Invitemeto: (Gid) 
║╠❂➣ Acc invite 
║╠❂➣ Removechat 
║╠❂➣ Qr on/off 
║╠❂➣ Autokick on/off 
║╠❂➣ Ghost on/off 
║╠❂➣ Autocancel on/off 
║╠❂➣ Invitepro on/off 
║╠❂➣ Join on/off 
║╠❂➣ Joincancel on/off 
║╠❂➣ Respon on/off 
║╠❂➣ Responkick on/off 
║╠❂➣ Leave on/off 
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

helpMessage ="""
╔═════════════
║ Ayane Selfbot
╠═════════════
║ HELP COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Help self 
║╠❂➣ Help bot 
║╠❂➣ Help group 
║╠❂➣ Help set 
║╠❂➣ Help media 
║╠❂➣ Help admin 
║╠❂➣ Help creator 
║╠❂➣ Owner 
║╠❂➣ Admin 
║╠❂➣ Speed 
║╠❂➣ Speed test 
║╠❂➣ Status
║╚════════════
╠═════════════
║ Selfbot Ayane
║ Dibawah tanggung jawab NvStar
║ Hubungi admin dibawah ini
║ Jika ada keluhan
║ line.me/ti/p/~KazeReborn
╚═════════════
"""


KAC=[aldier]
mid = aldier.getProfile().mid
Bots=[mid]
Creator=["u529ed08e968ba9d107784186eb66b76a"]
admin=["u529ed08e968ba9d107784186eb66b76a","ua5f2cbc325816777be5ef529eb920c50"]

contact = aldier.getProfile()
backup1 = aldier.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = aldier.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "AutoJoin":False,
    "AutoJoinCancel":True,
    "memberscancel":5,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'likeOn':{},
    'detectMention':True,
    'kickMention':False,      
    'timeline':False,
    "Timeline":False,
    "comment":"",    
    "commentOn":False,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":True,
    "Ghost":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
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
       
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       aldier.sendMessage(msg)
    except Exception as error:
       print error

def mention2(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       aldier.sendMessage(msg)
    except Exception as error:
       print error


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
    return '║╠❂➣ %02d Hari\n║╠❂➣ %02d Jam\n║╠❂➣ %02d Menit\n║╠❂➣ %02d Detik\n' % (days ,hours, mins, secs)      
    
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
              aldier.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                aldier.sendText(op.param1,str(wait["message"]))


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
                            Name = aldier.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        aldier.sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        aldier.sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                else:
                                    aldier.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            aldier.leaveRoom(op.param1)

        if op.type == 21:
            aldier.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    aldier.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = aldier.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        aldier.acceptGroupInvitation(op.param1)
                        aldier.sendText(op.param1,"Maaf " + aldier.getContact(op.param2).displayName + "\nMember Kurang Dari 5 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        aldier.leaveGroup(op.param1)                        
		    else:
                        aldier.acceptGroupInvitation(op.param1)
			aldier.sendText(op.param1," ☆ Hay Salken ^_^  ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = aldier.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        aldier.rejectGroupInvitation(op.param1)
		    else:
                        aldier.acceptGroupInvitation(op.param1)
			aldier.sendText(op.param1," ☆ Hallo semuanyaa~ Salken ^_^  ☆")
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    aldier.cancelGroupInvitation(op.param1,[op.param3])
                    aldier.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    aldier.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = aldier.getGroup(op.param1)
            contact = aldier.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            aldier.sendText(op.param1,"Hallo " + aldier.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            aldier.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            aldier.sendText(op.param1,"Good Bye " + aldier.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                aldier.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = aldier.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  aldier.sendText(msg.to,ret_)
                                  aldier.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = aldier.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  aldier.sendText(msg.to,ret_)
                                  break              


        if op.type == 25:
            msg = op.message


            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    aldier.sendChatChecked(msg.from_,msg.id)
                else:
                    aldier.sendChatChecked(msg.to,msg.id)
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     aldier.like(url[25:58], url[66:], likeType=1005)
                     aldier.comment(url[25:58], url[66:], wait["comment"])
                     aldier.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            aldier.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            aldier.sendText(msg.to,"Ditambahkan")
		    else:
			aldier.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        aldier.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        aldier.sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     aldier.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = aldier.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = aldier.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         aldier.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = aldier.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = aldier.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         aldier.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = aldier.getGroup(msg.to)
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
                        aldier.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        aldier.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        aldier.sendText(msg.to,"Can not be used outside the group")
                    else:
                        aldier.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                aldier.sendMessage(msg)
		
            elif msg.text in ["Admin","admin"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                aldier.sendMessage(msg)                
                aldier.sendText(msg.to,"Itu Admin Kami (^_^)")	
		
 
                
            elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = aldier.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   aldier.sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            aldier.sendText(msg.to,"Admin aldierG Ditambahkan")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                aldier.sendText(msg.to,"Command Denied.")
                aldier.sendText(msg.to,"Creator Permission Required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = aldier.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   aldier.sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            aldier.sendText(msg.to,"Admin aldierG Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                aldier.sendText(msg.to,"Command Denied.")
                aldier.sendText(msg.to,"Creator Permission Required.")
                
            elif msg.text in ["Admin list","admin list","List admin"]:
              if admin == []:
                  aldier.sendText(msg.to,"The Admin List Is Empty")
              else:
                  aldier.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════════════\n║        ☆☞ LIST ADMIN ☜☆\n╠═════════════════════\n"
                  for mi_d in admin:
                      mc += "╠••> " +aldier.getContact(mi_d).displayName + "\n"
                  aldier.sendText(msg.to,mc + "╚═════════════════════")
                  print "[Command]Admin List executed"
                 

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = aldier.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                aldier.sendMessage(msg)
		aldier.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    aldier.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = aldier.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                aldier.findAndAddContactsByMid(target)
                                contact = aldier.getContact(target)
                                cu = aldier.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                aldier.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                aldier.sendText(msg.to,"Profile Picture " + contact.displayName)
                                aldier.sendImageWithURL(msg.to,image)
                                aldier.sendText(msg.to,"Cover " + contact.displayName)
                                aldier.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = aldier.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                aldier.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                aldier.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = aldier.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             aldier.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 aldier.findAndAddContactsByMid(target)
                                 aldier.inviteIntoGroup(msg.to,[target])
                                 aldier.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      aldier.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key 1","help 1","Help 1","Help creator"]:
                aldier.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key 2","help 2","Help 2","Help group"]:
                aldier.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                aldier.sendText(msg.to,helpMessage)

            elif msg.text in ["Key 3","help 3","Help 3","Help self"]:
                aldier.sendText(msg.to,selfMessage)

            elif msg.text in ["Key 4","help 4","Help 4","Help bot"]:
                aldier.sendText(msg.to,botMessage)

            elif msg.text in ["Key 5","help 5","Help 5","Help set"]:
                aldier.sendText(msg.to,setMessage)

            elif msg.text in ["Key 6","help 6","Help 6","Help media"]:
                aldier.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key 7","help 7","Help 7","Help admin"]:
                aldier.sendText(msg.to,adminMessage)                
                

 
            elif msg.text in ["List group"]:
                    gid = aldier.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = aldier.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    aldier.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = aldier.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = aldier.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    aldier.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    aldier.sendText(msg.to, "Khusus Admin")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        aldier.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +aldier.getGroup(gid).name + "\n"
                        aldier.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    aldier.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if aldier.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    aldier.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    aldier.sendText(msg.to, "Khusus Ayane")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = aldier.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = aldier.getGroup(i).name
		            if h == ng:
		                aldier.inviteIntoGroup(i,[Creator])
			        aldier.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        aldier.sendText(msg.to,"Khusus Ayane")
		except Exception as e:
		    aldier.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = aldier.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = aldier.getGroup(i).name
		        if h == ng:
			    aldier.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            aldier.leaveGroup(i)
			    aldier.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")
 
	    elif "Leave all group" == msg.text:
		gid = aldier.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			aldier.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        aldier.leaveGroup(i)
		    aldier.sendText(msg.to,"Success Leave All Group")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = aldier.getGroupIdsJoined()
                for i in gid:
                    h = aldier.getGroup(i).name
                    gna = aldier.getGroup(i)
                    if h == saya:
                        aldier.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = aldier.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        aldier.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        aldier.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    aldier.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = aldier.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    aldier.updateGroup(X)
                    aldier.sendText(msg.to,"Url Sudah Aktif")
                else:
                    aldier.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = aldier.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    aldier.updateGroup(X)
                    aldier.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    aldier.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    aldier.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    aldier.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    aldier.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    aldier.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")		    
		    
 
            elif msg.text in ["Respon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    aldier.sendText(msg.to,"Auto Respon Sudah Aktif")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")

            elif msg.text in ["Respon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    aldier.sendText(msg.to,"Auto Respon Sudah Off")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")	
		    
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    aldier.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    aldier.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                aldier.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    aldier.sendText(msg.to,"Khusus Ayane")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                aldier.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    aldier.sendText(msg.to,"Khusus Ayane")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                aldier.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    aldier.sendText(msg.to,"Khusus Ayane")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                aldier.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    aldier.sendText(msg.to,"Khusus Ayane")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	aldier.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    aldier.sendText(msg.to,"Khusus Ayane")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	aldier.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    aldier.sendText(msg.to,"Khusus Ayane")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     aldier.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        aldier.sendText(msg.to,"Khusus Ayane")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     aldier.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        aldier.sendText(msg.to,"Khusus Ayane")	     

	    elif "Ghost on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = True
		     aldier.sendText(msg.to,"Ghost Sudah Aktif")
	     else:
	        aldier.sendText(msg.to,"Khusus Ayane")		     

	    elif "Ghost off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = False
		     aldier.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
	     else:
	         aldier.sendText(msg.to,"Khusus Ayane")		     

            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    wait["Ghost"] = True                     
                    aldier.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    wait["Ghost"] = False                    
                    aldier.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    aldier.sendText(msg.to,"Khusus Ayane")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                aldier.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                aldier.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                aldier.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                aldier.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        aldier.sendText(msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        aldier.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        aldier.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        aldier.sendText(msg.to,"Sudah Off(p′︵‵。)")
                        
                        
            elif "Cyduk on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                aldier.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Cyduk off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    aldier.sendText(msg.to, "Cek Sider Off")
                else:
                    aldier.sendText(msg.to, "Heh Belom Di Set")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠➩✔️ Sambutan : On\n"
		else:md+="╠➩❌ Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                else: md +="╠➩❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                else: md +="╠➩❌ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
		else: md+="╠➩❌ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                else: md+= "╠➩❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                else: md+= "╠➩❌ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
		else:md+="╠➩❌ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
		else:md+="╠➩❌ Auto Kick : Off\n"
		if wait["Ghost"] == True: md+="╠➩✔️ Ghost : On\n"
		else:md+="╠➩❌ Ghost : Off\n"
		if wait["alwaysRead"] == True: md+="╠➩✔️ Always Read : On\n"
		else:md+="╠➩❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠➩✔️ Auto Respon : On\n"
		else:md+="╠➩❌ Auto Respon : Off\n"		
		if wait["kickMention"] == True: md+="╠➩✔️ Auto Respon Kick : On\n"
		else:md+="╠➩❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠➩✔️ Auto Sider : On\n"
		else:md+="╠➩❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠➩✔️ Simisimi : On\n"
		else:md+="╠➩❌ Simisimi: Off\n"		
                aldier.sendText(msg.to,"╔═══════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═══════════════════\n"+md+"╚═══════════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                aldier.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = aldier.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    aldier.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    aldier.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)
                
        


            elif msg.text in ["Tagall","Tag all"]:
            	 if msg.from_ in admin:              
                    group = aldier.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        mention2(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                        mention2(msg.to, nm1)
                        for j in range(101, len(nama)):
                            nm2 += [nama[j]]
                        mention2(msg.to, nm2)
                    if jml > 200 and jml < 300:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                        mention2(msg.to, nm1)
                        for j in range(101, 200):
                            nm2 += [nama[j]]
                        mention2(msg.to, nm2)
                        for k in range(201, len(nama)):
                            nm3 += [nama[k]]
                        mention2(msg.to, nm3)
                    if jml > 300 and jml < 400:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                        mention2(msg.to, nm1)
                        for j in range(101, 200):
                            nm2 += [nama[j]]
                        mention2(msg.to, nm2)
                        for k in range(201, 300):
                            nm3 += [nama[k]]
                        mention2(msg.to, nm3)
                        for l in range(301, len(nama)):
                            nm4 += [nama[l]]
                        mention2(msg.to, nm4)
                    if jml > 400 and jml < 500:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                        mention2(msg.to, nm1)
                        for j in range(101, 200):
                            nm2 += [nama[j]]
                        mention2(msg.to, nm2)
                        for k in range(201, 300):
                            nm3 += [nama[k]]
                        mention2(msg.to, nm3)
                        for l in range(301, 400):
                            nm4 += [nama[l]]
                        mention2(msg.to, nm4)
                        for h in range(401, len(nama)):
                            nm5 += [nama[h]]
                        mention2(msg.to, nm5)
                    if jml > 500:
                        aldier.sendText(msg.to,'Member melebihi batas.')
                    cnt = Message()
                    cnt.text = "Done : " + str(jml) +  " Members"
                    cnt.to = msg.to
                    aldier.sendMessage(cnt)


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                aldier.sendText(msg.to, "☆Checkpoint Checked☆")
                print "Setview"

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
                    contactId = aldier.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════"
                        aldier.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        aldier.sendText(msg.to, "☆Auto Checkpoint☆")                        
                    else:
                        aldier.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    aldier.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    aldier.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = aldier.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    aldier.findAndAddContactsByMids(mi_d)
		    aldier.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                aldier.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                aldier.sendText(msg.to,"Shere Post Kamu Yang Mau Di Like!")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                aldier.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                aldier.sendText(msg.to,"Send Contact") 
                

	    elif "Recover" in msg.text:
		thisgroup = aldier.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		aldier.createGroup("Recover", mi_d)
		aldier.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = aldier.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    aldier.updateGroup(X)
                else:
                    aldier.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    aldier.kickoutFromGroup(msg.to,[midd])
		else:
		    aldier.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                aldier.findAndAddContactsByMid(midd)
                aldier.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "u1541ccc69edf22556861a136659b51e6"
                aldier.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = aldier.getGroup(msg.to)
                aldier.sendText(msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                aldier.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = aldier.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			aldier.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~aldiergokil04")
		    aldier.sendText(msg.to,"Success BC BosQ")
		else:
		    aldier.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = aldier.getGroupIdsInvited()
                for i in gid:
                    aldier.rejectGroupInvitation(i)
                aldier.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = aldier.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        aldier.updateGroup(x)
                    gurl = aldier.reissueGroupTicket(msg.to)
                    aldier.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        aldier.sendText(msg.to,"Can't be used outside the group")
                    else:
                        aldier.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = aldier.activity(limit=5)
		    aldier.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    aldier.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		aldier.sendText(msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                aldier.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		aldier.sendText(msg.to, "Progress...")
                aldier.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                aldier.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                aldier.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    aldier.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    aldier.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = aldier.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        aldier.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    aldier.sendText(msg.to,"Succes BosQ")
                                except:
                                    aldier.sendText(msg.to,"Error")
			    else:
				aldier.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    aldier.sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +aldier.getContact(mi_d).displayName + "\n"
                    aldier.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = aldier.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        aldier.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                aldier.sendText(msg.to,"Succes BosQ")
                            except:
                                aldier.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    aldier.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

            elif msg.text.lower() in ["bot","aldierG"]:
                aldier.sendText(msg.to,"Apa Manggil~Manggil Aku!?") 
                aldier.sendText(msg.to,"☆Ketik ☞Help☜ Untuk Bantuan☆") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = aldier.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            aldier.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            aldier.kickoutFromGroup(msg.to,[jj])
                        aldier.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    aldier.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = aldier.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            aldier.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                aldier.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
  #          elif "Kickall" == msg.text:
#		    if msg.from_ in Creator:
 #                    if msg.toType == 2:
  #                      print "Kick all member"
   #                     _name = msg.text.replace("Kickall","")
#                        gs = aldier.getGroup(msg.to)
#                        aldier.sendText(msg.to,"Dadaaah~")
#                        targets = []
#                        for g in gs.members:
#                            if _name in g.displayName:
#                                targets.append(g.mid)
#                        if targets == []:
#                            aldier.sendText(msg.to,"Not found.")
#                        else:
#                            for target in targets:
#				if target not in admin:
 #                                   try:
  #                                      aldier.kickoutFromGroup(msg.to,[target])
   #                                     print (msg.to,[g.mid])
    #                                except Exception as e:
     #                                   aldier.sendText(msg.to,str(e))
			    
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    aldier.sendText(msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    aldier.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    

 
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = aldier.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       aldier.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               aldier.CloneContactProfile(target)
                               aldier.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    aldier.updateDisplayPicture(backup1.pictureStatus)
                    aldier.updateProfile(backup1)
                    aldier.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    aldier.sendText(msg.to, str(e))

 
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						aldier.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						aldier.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						aldier.sendAudioWithURL(msg.to,abc)
						aldier.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
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
                        aldier.sendText(msg.to, hasil)
                except Exception as wak:
                        aldier.sendText(msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						aldier.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						aldier.sendAudioWithURL(msg.to,abc)
						aldier.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						aldier.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    aldier.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"
                    
            elif "Spam " in msg.text:
              if msg.from_ in admin and Creator:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 10000:
                              for x in range(jmlh):
                                aldier.sendText(msg.to, teks)
                        else:
                                aldier.sendText(msg.to, "Out of range! ")
                    elif txt[1] == "off":
                          if jmlh <= 10000:
                                aldier.sendText(msg.to, tulisan)
                          else:
                                aldier.sendText(msg.to, "Out of range! ")
                                
            elif "Spamcontact @" in msg.text:
                if msg.from_ in Creator:
                    _name = msg.text.replace("Spamcontact @","")
                    _nametarget = _name.rstrip(' ')
                    gs = aldier.getGroup(msg.to)
                    for g in gs.members:
                      if _nametarget == g.displayName:
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Ini Adalah Spam")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Jangan Ngintip")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(g.mid,"Masuk Room Woy")
                        aldier.sendText(msg.to, "Target Spam, Done...!!!")
                        print " Spammed !"

                else:
                    aldier.sendText(msg.to, "No Access")


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = aldier.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        aldier.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = aldier.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                aldier.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                aldier.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = aldier.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        aldier.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = aldier.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                aldier.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                aldier.sendText(msg.to,"Upload image failed.")
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = aldier.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        aldier.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = aldier.getContact(target)
                                aldier.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                aldier.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = aldier.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        aldier.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = aldier.getContact(target)
                                aldier.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                aldier.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["#"]
                                pilih = random.choice(link)
                                aldier.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    aldier.sendText(msg.to, (bctxt))
                    t-=1

#            elif "Scbc " in msg.text:
#                  bctxt = msg.text.replace("Scbc ", "")
#                  orang = aldier.getAllContactIds()
#                  t = 20
#                  for manusia in orang:
#                    while(t):
#                      aldier.sendText(manusia, (bctxt))
#                      t-=1

 #           elif "Cbc " in msg.text:
  #                broadcasttxt = msg.text.replace("Cbc ", "") 
 #                 orang = aldier.getAllContactIds()
  #                for manusia in orang:
  #                  aldier.sendText(manusia, (broadcasttxt))

 
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
                    detail = "====INSTAGRAM INFO====\n"
                    details = "\n====INSTAGRAM INFO===="
                    aldier.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    aldier.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	aldier.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                aldier.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                aldier.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    aldier.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    aldier.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        aldier.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        aldier.sendText(msg.to, "Could not find it")                    

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = aldier.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +aldier.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    aldier.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                aldier.sendText(msg.to,"Sedang Mencari...")
                aldier.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                aldier.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = aldier.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        aldier.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = aldier.getProfile()
                        profile.statusMessage = string
                        aldier.updateProfile(profile)
                        aldier.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = aldier.getProfile()
                        profile.displayName = string
                        aldier.updateProfile(profile)
                        aldier.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +aldier.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                aldier.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                aldier.sendMessage(msg)

            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")                


            elif "berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                aldier.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                aldier.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                aldier.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    aldier.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        aldier.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                aldier.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                aldier.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                aldier.sendText(msg.to, A)                

            
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
                aldier.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


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
                aldier.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                aldier.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                aldier.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = aldier.getAllContactIds()
                kontak = aldier.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                aldier.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = aldier.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                aldier.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = aldier.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    aldier.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = aldier.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            aldier.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = aldier.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                aldier.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = aldier.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                aldier.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = aldier.getContact(key1)
                cu = aldier.channel.getCover(key1)
                try:
                    aldier.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    aldier.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = aldier.getContact(key1)
                cu = aldier.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    aldier.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    aldier.sendText(msg.to,"Profile Picture " + contact.displayName)
                    aldier.sendImageWithURL(msg.to,image)
                    aldier.sendText(msg.to,"Cover " + contact.displayName)
                    aldier.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = aldier.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                aldier.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = aldier.getContact(key1)
                cu = aldier.channel.getCover(key1)
                try:
                    aldier.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    aldier.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = aldier.getContact(key1)
                cu = aldier.channel.getCover(key1)
                try:
                    aldier.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    aldier.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "╔═════════════\n║ SELF BOT\n║ Telah Berjalan\n║ Selama\n╠═════════════\n║╔════════════\n" + waktu(eltime) + "║╚════════════\n╚═════════════\n"
                aldier.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                aldier.sendText(msg.to,"====== I N F O R M A S I ======\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n====== I N F O R M A S I ======")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
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
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                aldier.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = aldier.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                aldier.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = aldier.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                aldier.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        aldier.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        aldier.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        aldier.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        aldier.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            aldier.findAndAddContactsByMid(msg.from_)
                            aldier.inviteIntoGroup(gid,[msg.from_])
                        except:
                            aldier.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                aldier.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = aldier.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (aldier.getGroup(i).name +" ~> ["+str(len(aldier.getGroup(i).members))+"]")
                aldier.sendText(msg.to,"╔═════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════\n" + h + "╠═════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = aldier.getGroupIdsJoined()
                kontak = aldier.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                aldier.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    aldier.sendText(msg.to,"Sedang Mencari...")
                    aldier.sendText(msg.to, "https://www.google.com/" + b)
                    aldier.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        aldier.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = aldier.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            aldier.sendText(msg.to,h)
                        except Exception as error:
                            aldier.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = aldier.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                aldier.rejectGroupInvitation(i)
                            except:
                                aldier.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        aldier.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        aldier.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = aldier.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = aldier.getGroup(i)
                            _list += gids.name
                            aldier.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        aldier.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        aldier.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = aldier.fetchOps(aldier.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(aldier.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            aldier.Poll.rev = max(aldier.Poll.rev, Op.revision)
            bot(Op)


# -*- coding: utf-8 -*-
#Chucky_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
from socket import error as SocketError
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile,wikipedia

cl = LINETCR.LINE() #NvStar Captain
cl.login(token='Ep2tjCyxj75wgf0RUWpb.9ji8SkFfgD8JtZs6ydV82W.WN33OtrIXLQPxzhTt22k3gI7/rKq6lbBEZnb5FGo6do=')
cl.loginResult()

#ki = LINETCR.LINE() #NvStar Protection 2
#ki.login(token='Ep2tjCyxj75wgf0RUWpb.9ji8SkFfgD8JtZs6ydV82W.WN33OtrIXLQPxzhTt22k3gI7/rKq6lbBEZnb5FGo6do=')
#ki.loginResult()

kk = LINETCR.LINE() #NvStar Protection 3
kk.login(token='EpE5sCyEnTXEEwUT1Ae3.jdyOWRLffB6A0N6J2PyaWW.XdJz30IFf+5LUrcYTniT1sMg2YIGJxNP5+tRAWQP9dE=')
kk.loginResult()

kc = LINETCR.LINE() #NvStar Protection 4
kc.login(token='Ep2lWopsvibKmXXxHC9d.4xpugoN02ultPiyRgGiahq.82mlL+YdW5n4x9lDGJjNZZl7plBGwqXDGov4dysHCZg=')
kc.loginResult()

ks = LINETCR.LINE() #NvStar Protection 5
ks.login(token='Ep0sMwfRo7qT31RJ1wQ3.BhXPEnTSoV/wf8Am4MRdiW.GldgH4hpDcrhWXo1GjXf2jdjbgUqRIVVeDzGb53HmKU=')
ks.loginResult()

ki = cl

print "NvStar Protection Success Login"
reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
╔═════════════
║ NvStar BOT v8.5.0
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
║╠❂➣ Getbio @ 
║╠❂➣ Friendlist 
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

botMessage ="""
╔═════════════
║ NvStar BOT v8.5.0
╠═════════════
║ BOT COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Absen 
║╠❂➣ Respon 
║╠❂➣ Runtime 
║╠❂➣ Nvcaptain copy @ 
║╠❂➣ Nv1 copy @ 
║╠❂➣ Nv2 copy @ 
║╠❂➣ Nv3 copy @ 
║╠❂➣ Nv4 copy @ 
║╠❂➣ Backup all 
║╠❂➣ /bio Text 
║╠❂➣ @bye (Usir Kapten) 
║╠❂➣ Bye all (Usir Semua) 
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

mediaMessage ="""
╔═════════════
║ NvStar BOT v8.5.0
╠═════════════
║ MEDIA COMMAND 
╠═════════════
║╔════════════
║╠❂➣ All gift 
║╠❂➣ Google: 
║╠❂➣ Playstore [NamaApp] 
║╠❂➣ Fancytext: Text 
║╠❂➣ .musik [Judul-Penyanyi]
║╠❂➣ .lirik [Judul-Penyanyi]
║╠❂➣ .musrik [Judul-Penyanyi]
║╠❂➣ /ig [Ursname] 
║╠❂➣ Checkig [Ursname] 
║╠❂➣ Apakah 
║╠❂➣ Kapan
║╠❂➣ Hari
║╠❂➣ Berapa
║╠❂➣ Berapakah 
║╠❂➣ wikipedia [text]
║╠❂➣ .Youtubelink: 
║╠❂➣ .Youtubevideo:
║╠❂➣ .Youtubesearch:
║╠❂➣ Image NamaGambar 
║╠❂➣ Say-id 
║╠❂➣ Say-en 
║╠❂➣ Say-jp 
║╠❂➣ Image
║╠❂➣ Tr-id
║╠❂➣ Tr-en
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
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

groupMessage ="""
╔═════════════
║ NvStar BOT v8.5.0
╠═════════════
║ GROUP COMMAND 
╠═════════════
║╔════════════
║╠❂➣ .welcome 
║╠❂➣ Invite creator 
║╠❂➣ Set
║╠❂➣ Check
║╠❂➣ Gn (NamaGroup) 
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
║╠❂➣ Kick (Mid) 
║╠❂➣ Invite: (Mid) 
║╠❂➣ Invite 
║╠❂➣ Memlist 
║╠❂➣ Getgroup image 
║╠❂➣ Urlgroup Image 
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""
WIB="ua5f2cbc325816777be5ef529eb920c50"

creatorMessage ="""
╔═════════════
║ NvStar BOT v8.5.0
╠═════════════
║ CREATOR COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Admin add @ 
║╠❂➣ Admin remove @ 
║╠❂➣ Cn
║╠❂➣ Bc: (Text) 
║╠❂➣ Nk: @ 
║╠❂➣ Join group: (NamaGroup)
║╠❂➣ Leave group: (NamaGroup)
║╠❂➣ Leave all group 
║╠❂➣ Tag on/off 
║╠❂➣ ifconfig
║╠❂➣ system
║╠❂➣ kernel
║╠❂➣ cpu
║╠❂➣ Reboot
║╠❂➣ Turn off 
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

adminMessage ="""
╔═════════════
║ NvStar BOT v8.5.0
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
║╠❂➣ All join / (TC1/2/3/4 Join) 
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

helpMessage ="""
╔═════════════
║ NvStar BOT v8.5.0
╠═════════════
║ HELP COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Help self 
║╠❂➣ Help bot 
║╠❂➣ Help group 
║╠❂➣ Help media 
║╠❂➣ Help admin 
║╠❂➣ Help creator 
║╠❂➣ Owner 
║╠❂➣ Speed 
║╠❂➣ Speed test
║╠❂➣ Set view
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

KAC=[cl,ki,kk,kc,ks]
mid = cl.getProfile().mid #NvStar Captain
Amid = ki.getProfile().mid #NvStar Protection 2
Bmid = kk.getProfile().mid #NvStar Protection 3
Cmid = kc.getProfile().mid #NvStar Protection 4
Dmid = ks.getProfile().mid #NvStar Protection 5

Bots=[mid,Amid,Bmid,Cmid,Dmid]
admin=["ua5f2cbc325816777be5ef529eb920c50","u354838cfb35216ada4dcfc789de6f205","uc33e556c10279d1ba84669b303da74dd","u6f1809a9977fc0e6de0ae8f740e03922","uce3f3af0c36f4bf099972c0a5687ed42","u15a96ad4cce3ed4f4a03513cad7ad822","u529ed08e968ba9d107784186eb66b76a","uaa81f36f1d8d1c9105aa347d3fee442b","u2d7040967b3413bc7e0c47800f0b71b5","u04ed2796b2b055f6ee910fe11f4592a4","u1592572d68b3f7bf057e28bd01334651","u467aea8464c96bd16b09a43ea9adb70e","u2de145ff1f62b6b416fc437dbd768c81","u9cdc29cb1452168cadae627171b7a6ee","u7e437bac03aaa65bbe6255248f866574","u6e7a86a6209dae80af12cbf920eabea7","ue9fdcde9aab0d6f87d2ace7f21a01802"]
Creator=["ua5f2cbc325816777be5ef529eb920c50"]
whitelist=[""]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"NvStar Captain ",
    "cName2":"NvStar Protection 2 ",
    "cName3":"NvStar Protection 3 ",
    "cName4":"NvStar Protection 4 ",
    "cName5":"NvStar Protection 5 ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectcancl":False,
    "protectionOn":True,
    "atjointicket":True
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
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
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
                                        cl.sendText(op.param1, "Hayoo~ " + nick[0] + "\nKetahuan deh 􀜁􀅔Har Har􏿿 ")
                                    else:
                                        cl.sendText(op.param1, "Cilukba... " + nick[1] + "\nKetahuan deh 􀜁􀅔Har Har􏿿")
                                else:
                                    cl.sendText(op.param1, "Nahh looh~ " + Name + "\nKetahuan deh 􀜁􀅔Har Har􏿿")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass



        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                try:
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Tolong QR codenya jangan dibuka")
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  X = cl.getGroup(op.param1)
                  X.preventJoinByTicket = True
                  cl.updateGroup(X)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Tolong QR codenya jangan dibuka")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(Z)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
              random.choice(KAC).sendText(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or Creator:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or Creator:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or Creator:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or Creator:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or Creator:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                    
        #------Joined User Kick start------#
        #if op.type == 17: #awal 17 ubah 13
           #if wait["Protectjoin"] == True:
               #if op.param2 not in admin and Bots : # Awalnya admin doang
                   #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            try:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
              #f=codecs.open('st2__b.json','w','utf-8')
              #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
              #f=codecs.open('st2__b.json','w','utf-8')
              #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
              
        if op.type == 19: #bot Ke Kick
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = ki.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Bmid:
              if op.param2 not in Bots or admin:
                try:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) 
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Cmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ks.getGroup(op.param1)
                  ks.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) 
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Dmid:
              if op.param2 not in Bots or admin:
                try:
                  G = cl.getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) 
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in admin:
              if op.param2 not in Bots:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[admin])
                    wait["blacklist"][op.param2] = True
                  except:
                    try:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                      wait["blacklist"][op.param2] = True
                  
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#==========Help Start==========
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,adminMessage)  

            elif msg.text in ["Key self","help self","Help self"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,botMessage)

            elif msg.text in ["Key media","help media","Help media"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin",]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,adminMessage)   
#==========Help Finish=========t)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Nv2gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Nv3gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Nv4gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Nv2invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Nv3invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "nv4invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
              
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in Creator:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Creator=--------------
            elif "Nc " in msg.text:
              if msg.from_ in Creator:
                string = msg.text.replace("Nc ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
#            elif "Spam: " in msg.text:
#              if msg.from_ in admin:
#                txt = msg.text.split(" ")
#                jmlh = int(txt[2])
#                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
#                tulisan = jmlh * (teks+"\n")
#                 #@reno.a.w
#                if txt[1] == "on":
#                    if jmlh <= 300:
#                       for x in range(jmlh):
#                           cl.sendText(msg.to, teks)
#                    else:
#                       cl.sendText(msg.to, "Kelebihan batas:v")
#                elif txt[1] == "off":
#                    if jmlh <= 300:
#                        cl.sendText(msg.to, tulisan)
#                    else:
#                        cl.sendText(msg.to, "Kelebihan batas :v")
    #-----------------=Selesai=------------------
#            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
#              if msg.from_ in admin:
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': mid}
#                cl.sendMessage(msg)

#                msg.contentType = 13
#                msg.contentMetadata = {'mid': Amid}
#                ki.sendMessage(msg)

#                msg.contentType = 13
#                msg.contentMetadata = {'mid': Bmid}
#                kk.sendMessage(msg)

#                msg.contentType = 13
#                msg.contentMetadata = {'mid': Cmid}
#                kc.sendMessage(msg)
                
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': Dmid}
#                ks.sendMessage(msg)
                
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
#              if msg.from_ in admin:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '5'}
#                msg.text = None
#                random.choice(KAC).sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
#              if msg.from_ in admin:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '12'}
#                msg.text = None
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            cl.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Tidak ada satu orang pun yang masuk dalam daftar pending group")
                            else:
                                cl.sendText(msg.to,"Sorry, nobody absent")

            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"Tidak ada invite pending")
                        else:
                            k3.sendText(msg.to,"Tidak ada invite pending")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        k3.sendText(msg.to,"Tidak dapat digunakan diluar group")

            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)

            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"QR Sudah Terbuka")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Tidak dapat digunakan diluar group")

            elif msg.text in ["Nv2qr on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"QR sudah dibuka")
                    else:
                        cl.sendText(msg.to,"QR sudah terbuka")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")

            elif msg.text in ["Nv3qr on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"QR sudah dibuka")
                    else:
                        ki.sendText(msg.to,"QR sudah terbuka")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        ki.sendText(msg.to,"Tidak dapat digunakan diluar group")
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi Creator kami dibawah ini")
                cl.sendMessage(msg)

            elif msg.text in ["Nv4qr on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"QR sudah dibuka")
                    else:
                        kc.sendText(msg.to,"QR sudah terbuka")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        kc.sendText(msg.to,"Tidak dapat digunakan diluar group")
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi Creator kami dibawah ini")
                cl.sendMessage(msg)

            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Tidak dapat digunakan diluar group")
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi Creator kami dibawah ini")
                cl.sendMessage(msg)


            elif msg.text in ["Nv2qr off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"QR code sudah ditutup")
                    else:
                        ki.sendText(msg.to,"QR code sudah tertutup")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        ki.sendText(msg.to,"Tidak dapat digunakan diluar group")
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi Creator kami dibawah ini")
                cl.sendMessage(msg)


            elif msg.text in ["Nv3qr off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"QR code sudah ditutup")
                    else:
                        kk.sendText(msg.to,"QR code sudah tertutup")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        kk.sendText(msg.to,"Tidak dapat digunakan diluar group")
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi Creator kami dibawah ini")
                cl.sendMessage(msg)

            elif msg.text in ["Nv4qr off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"QR code sudah ditutup")
                    else:
                        kc.sendText(msg.to,"QR code sudah tertutup")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        kc.sendText(msg.to,"Tidak dapat digunakan diluar group")
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi Creator kami dibawah ini")
                cl.sendMessage(msg)


            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                
            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
#            elif "Mid Bot" == msg.text:
#              if msg.from_ in admin:
#                cl.sendText(msg.to,mid)
#                ki.sendText(msg.to,Amid)
#                kk.sendText(msg.to,Bmid)
#                kc.sendText(msg.to,Cmid)
#                ks.sendText(msg.to,Dmid)
#            elif "Koplaxs" == msg.text:
#              if msg.from_ in admin:
#                cl.sendText(msg.to,Smid)
#            elif "Luffy" == msg.text:
#              if msg.from_ in admin:
#                ki.sendText(msg.to,mid)
#            elif "Zorro" == msg.text:
#              if msg.from_ in admin:
#                kk.sendText(msg.to,Amid)
#            elif "Sanji" == msg.text:
#              if msg.from_ in admin:
#                kc.sendText(msg.to,Bmid)
#            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "100",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                cl.sendMessage(msg)
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "10",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Galau"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "9",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["You"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "7",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Hadeuh"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "6",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Please"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "4",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Haaa"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "3",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Lol"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "110",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "101",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#            elif msg.text in ["Welcome"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "247",
#                                     "STKPKGID": "3",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["TL: "]:
#              if msg.from_ in admin:
#                tl_text = msg.text.replace("TL: ","")
#                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif "Midcheck " in msg.text:
                mmid = msg.text.replace("Midcheck ","")
                msg.contentType = 13
                msg.contentMetadata = {'mid': mmid}
                cl.sendMessage(msg)
            #elif msg.text in ["Joinn on","joinn on"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == True:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"Done")
                #else:
                    #wait["Protectjoin"] = True
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"done")
            #elif msg.text in ["Joinn off","joinn off"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == False:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
                #else:
                    #wait["Protectjoin"] = False
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in Creator:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Join on","Auto join on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Join off","Auto join off"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Gcancel:"]:
              if msg.from_ in Creator:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Leave on","Auto leave:on"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave on dinyalakan")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Done")

            elif msg.text in ["Leave off","Auto leave:off"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave off dimatikan")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")


#            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
#              if msg.from_ in admin:
#                if wait["timeline"] == True:
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"already on")
#                    else:
#                        cl.sendText(msg.to,"done")
#                else:
#                    wait["timeline"] = True
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"done")
#                    else:
#                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
#            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
#              if msg.from_ in admin:
#                if wait["timeline"] == False:
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"already off")
#                    else:
#                        cl.sendText(msg.to,"done")
#                else:
#                    wait["timeline"] = False
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"done")
#                    else:
#                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Set view"]:
              if msg.from_ in admin:
                md = ""
                if wait["Protectgr"] == True: md+="║╠❂➣✔️ Protect QR [On]\n"
                else: md+="║╠❂➣❌ Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="║╠❂➣✔️ Protect Invite [On]\n"
                else: md+="║╠❂➣❌ Protect Invite [Off]\n"
                if wait["contact"] == True: md+="║╠❂➣✔️ Contact [On]\n"
                else: md+="║╠❂➣❌ Contact [Off]\n"
                if wait["autoJoin"] == True: md+="║╠❂➣✔️ Auto Join [On]\n"
                else: md +="║╠❂➣ Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="║╠❂➣ Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "║╠❂➣❌ Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="║╠❂➣✔️ Auto Leave [On]\n"
                else: md+="║╠❂➣❌ Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="║╠❂➣✔️ Share [On]\n"
                else:md+="║╠❂➣❌ Share [Off]\n"
                if wait["autoAdd"] == True: md+="║╠❂➣✔️ Auto Add [On]\n"
                else:md+="║╠❂➣❌ Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="║╠❂➣✔️ Comment [On]\n"
                else:md+="║╠❂➣❌ Comment [Off]"
                cl.sendText(msg.to,"╔═════════════════════════\n""║           ◄STATUS NvStar BOT►\n""╠═════════════════════════\n"+md+"╚═════════════════════════")


#            elif "album merit " in msg.text:
#                gid = msg.text.replace("album merit ","")
#                album = cl.getAlbum(gid)
#                if album["result"]["items"] == []:
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"There is no album")
#                    else:
#                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
#                else:
#                    if wait["lang"] == "JP":
#                        mg = "The following is the target album"
#                    else:
#                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
#                    for y in album["result"]["items"]:
#                        if "photoCount" in y:
#                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
#                        else:
#                            mg += str(y["title"]) + ":0sheet\n"
#                    cl.sendText(msg.to,mg)
#            elif "album " in msg.text:
#                gid = msg.text.replace("album ","")
#                album = cl.getAlbum(gid)
#                if album["result"]["items"] == []:
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"There is no album")
#                    else:
#                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
#                else:
#                    if wait["lang"] == "JP":
#                        mg = "The following is the target album"
#                    else:
#                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
#                    for y in album["result"]["items"]:
#                        if "photoCount" in y:
#                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
#                        else:
#                            mg += str(y["title"]) + ":0sheet\n"
#            elif "album remove " in msg.text:
#                gid = msg.text.replace("album remove ","")
#                albums = cl.getAlbum(gid)["result"]["items"]
#                i = 0
#                if albums != []:
#                    for album in albums:
#                        cl.deleteAlbum(gid,album["id"])
#                        i += 1
#                if wait["lang"] == "JP":
#                    cl.sendText(msg.to,str(i) + "Deleted albums")
#                else:
#                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")


            elif msg.text in ["Group id"]:
              if msg.from_ in Creator:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)

            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")


            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")


            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")


            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in Creator:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")


            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")


            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])

            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)

            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite Creator ke group------
            elif "invitemeto: " in msg.text:
              if msg.from_ in Creator:
                gid = msg.text.replace("invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    random.choice(KAC).findAndAddContactsByMid(msg.from_)
                    random.choice(KAC).inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in Creator:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
              if msg.from_ in admin:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

#Tempat SIDER
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Join all"]: #Panggil Semua Bot
              if msg.from_ in Creator:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                print "Semua Sudah Lengkap"
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["@Bye"]: #Bot Ninggalin Group termasuk Bot Induk
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Bye all"]: #Semua Bot Ninggalin Group Kecuali Bot Induk
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all","Tagall"]:
              if msg.from_ in Creator:
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
                      cl.sendText(msg.to,"Untuk admin...\nGunakanlah command ini dengan bijak.\nMungkin akan menggangu member lainnya")

                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)
        #----------------Fungsi Banned Kick Target Finish----------------------#                

#            elif "Ready op" in msg.text:
#              if msg.from_ in Creator:
#                if msg.toType == 2:
#                    print "ok"
#                    _name = msg.text.replace("Ready op","")
#                    gs = cl.getGroup(msg.to)
#                    gs = ki.getGroup(msg.to)
#                    gs = kk.getGroup(msg.to)
#                    gs = kc.getGroup(msg.to)
#                    gs = ks.getGroup(msg.to)
#                    random.choice(KAC).sendText(msg.to,"Eh Kontol Ini Room apaan?")
#                    random.choice(KAC).sendText(msg.to,"Ratain aja lah\nRoom Ga Berguna..")
#                    random.choice(KAC).sendText(msg.to,"Jangan Baper yah Tollll;")
#                    msg.contentType = 13
#                    msg.contentMetadata = {'mid': mid}
#                    random.choice(KAC).sendMessage(msg)
#                    targets = []
#                    for g in gs.members:
#                        if _name in g.displayName:
#                            targets.append(g.mid)
#                    if targets == []:
#                        random.choice(KAC).sendText(msg.to,"Not found")
#                    else:
#                        for target in targets:
#                          if target in Bots:
#                            pass
#                          elif target in admin:
#                            pass
#                          else:
#                            try:
#                              klist=[cl,ki,kk,kc,ks]
#                              kicker=random.choice(klist)
#                              kicker.kickoutFromGroup(msg.to,[target])
#                              print (msg.to,[g.mid])
#                            except:
#                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
#                              random.choice(KAC).sendText(msg.to,"Koq Ga Ditangkis Njiiing?\nLemah Banget Nih Room")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
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
                      cl.kickoutFromGroup(msg.to,[target])
                      print (msg.to,[g.mid])
                    except:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
        #----------------Fungsi Kick User Target Finish----------------------#

            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in Creator:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------

#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

#==========Check on/off sider start==========
            elif "Check on" in msg.text:
                if msg.from_ in Creator:
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
                    cl.sendText(msg.to,"Check sider one by one")
                
            elif "Check off" in msg.text:
                if msg.from_ in Creator:
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        wait["Sider"] = False
                        cl.sendText(msg.to, "Cek Sider Off")
                    else:
                        cl.sendText(msg.to, "[Check on] Belum aktiv")  
#==========Check on/off sider finish==========


#==========Check sider start==========
            elif msg.text in ["Setview","Setpoint","Cctv","Set"]:
              if msg.from_ in Creator:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Ketik [Check] untuk melihat sider")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
              if msg.from_ in Creator:
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
                        tukang = "╔═════════════════════════\n║         ◄SIDER LIST►\n╠═════════════════════════\n╠❂➣"
                        grp = '\n╠❂➣ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠❂➣ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                    else:
                        cl.sendText(msg.to, "Sider belum terlihat")
                    print "Viewseen"
#==========Check sider finish==========

#==========Search id start==========
            elif "SearchID: " in msg.text:
              if msg.from_ in Creator:
                userid = msg.text.replace("SearchID: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
              if msg.from_ in Creator:
                userid = msg.text.replace("Searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)
#==========Search id finish==========

#==========Checkdate start==========
            elif "Checkdate " in msg.text:
              if msg.from_ in Creator:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"[I N F O R M A S I]\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)
#==========Checkdate finish==========

#==========Kalender start==========
            elif "Checkdate " in msg.text:
              if msg.from_ in Creator:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"[I N F O R M A S I]\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)
#==========Kalender finish==========

#==========pp start==========
            elif "pp @" in msg.text:
              if msg.from_ in Creator:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
              if msg.from_ in Creator:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#==========pp finish==========

#===========Cover start==========
            elif "cover @" in msg.text:
              if msg.from_ in Creator:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
              if msg.from_ in Creator:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#===========Cover finish==========

#===========Get bio start==========
            elif "Getbio" in msg.text:
              if msg.from_ in Creator:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
#===========Get bio finish==========

#===========Friendlist start==========
            elif msg.text in ["Friendlist"]:   
              if msg.from_ in Creator:
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════[FRIEND LIST]═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════[FRIEND LIST]═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
#===========Friendlist finish==========

#===========Absen start==========
            elif msg.text in ["Absen"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Nv Captain STATUS: ONLINE")

            elif msg.text in ["Absen2"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Nv2 STATUS: ONLINE")

            elif msg.text in ["Absen3"]:
              if msg.from_ in admin:
                kk.sendText(msg.to,"Nv3 STATUS: ONLINE")

            elif msg.text in ["Absen4"]:
              if msg.from_ in admin:
                kc.sendText(msg.to,"Nv4 STATUS: ONLINE")

            elif msg.text in ["Absen5"]:
              if msg.from_ in admin:
                ks.sendText(msg.to,"Nv5 STATUS: ONLINE")
#===========Absen finish==========

#===========NvStar tagged start==========
            elif "@NvStar Captain" in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Hallo, jika membutuhkan sesuatu")
                cl.sendText(msg.to,"Silahkan PM/PC contact owner dibawah ini")
                cl.sendMessage(msg)
#===========NvStar tagged finish==========

            elif "@Agy ＼(^-^)／＼(^-^)／＼(^-^)／＼(^-^)／＼(^-^)／＼(^-^)／＼(^-^)／＼(^-^)／" in msg.text:
              if msg.from_ in Creator:
                jawab = ("Ada perlu apa lu sama majikan gue?","Mau ape lu haa??\nMajikan gue lagi kerja~~!!","Bacod lu jangan tag majikan gue","Mau ape lu?? majikan gue lagi ranked main osu.\nNih profilenya https://osu.ppy.sh/u/8599884","Sssshh~ tuh majikan gue lagi teriak teriak di smule\nkayak orang kesurupan􀜁􀅔Har Har􏿿\n\nhttps://www.smule.com/NvStar_","Oii majikan Kampret\nTemen lu manggil tuh~~!!!","Panggil terus bang majikan gue\nmemang agak budek")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)

#===========Absen all start==========
            elif msg.text in ["Absen all"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Nv Captain STATUS: ONLINE")
                ki.sendText(msg.to,"Nv2 STATUS: ONLINE")
                kk.sendText(msg.to,"Nv3 STATUS: ONLINE")
                kc.sendText(msg.to,"Nv4 STATUS: ONLINE")
                ks.sendText(msg.to,"Nv5 STATUS: ONLINE")
#===========Absen all finish==========


#===========Runtime start==========
            elif msg.text.lower() == 'runtime':
              if msg.from_ in admin:
                eltime = time.time() - mulai
                van = "╔═════════════\n║ NvStar BOT\n║ Telah Berjalan\n║ Selama\n╠═════════════\n║╔════════════\n" + waktu(eltime) + "║╚════════════\n╚═════════════\n"
                cl.sendText(msg.to,van)
#===========Runtime start==========

#===========Bio start==========
            elif ".bio " in msg.text:
                if msg.from_ in Creator:
                    string = msg.text.replace("/bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        ki.updateProfile(profile)
                        kk.updateProfile(profile)
                        kc.updateProfile(profile)
                        ks.updateProfile(profile)
                        cl.sendText(msg.to,"All Done")
#===========Bio Finish==========

#===========Copy start==========
            elif "Nvcaptain copy @" in msg.text:
              if msg.from_ in Creator:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Kapten copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif "Nv1 copy @" in msg.text:
              if msg.from_ in Creator:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC1 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif "Nv2 copy @" in msg.text:
              if msg.from_ in Creator:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC2 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kk.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kk.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kk.CloneContactProfile(target)
                               kk.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Nv3 copy @" in msg.text:
              if msg.from_ in Creator:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC3 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kc.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kc.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kc.CloneContactProfile(target)
                               kc.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e                                

            elif "Nv4 copy @" in msg.text:
              if msg.from_ in Creator:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC4 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ks.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ks.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ks.CloneContactProfile(target)
                               ks.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
#===========Copy finish==========

#==============================================================   MEDIA COMMAND   ==============================================================

#===========wikipedia start===========
            elif 'wikipedia ' in msg.text.lower():
              if msg.from_ in Creator:
                  try:
                      wiki = msg.text.lower().replace("wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Text Melebihi batas! Klik link dibawah ini untuk membaca\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#===========wikipedia start===========

						
#===========Google start===========
            elif "Google: " in msg.text:
              if msg.from_ in Creator:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Sedang Mencari...")
                    cl.sendText(msg.to, "https://www.google.com/" + b)
                    cl.sendText(msg.to,"Itu Dia Linknya. . .")     
#===========Google start===========

#===========Playstore start===========
            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                cl.sendText(msg.to,"Tuh Linknya Kak (^_^)")
#===========playstore finish===========

#===========Musik start===========
            elif ".musik " in msg.text:
              if msg.from_ in Creator:
                songname = msg.text.replace(".musik ","")
                params = {"songname": songname}
                r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    abc = song[3].replace('https://','http://')
                    cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
                    cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
                    cl.sendAudioWithURL(msg.to,abc)
                    cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif '.lirik ' in msg.text.lower():
              if msg.from_ in Creator:
                try:
                    songname = msg.text.lower().replace('.lirik ','')
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
                        
            elif ".musrik " in msg.text:
              if msg.from_ in Creator:
                songname = msg.text.replace(".musrik ","")
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
                    cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
                    cl.sendAudioWithURL(msg.to,abc)
                    cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
                    cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
#===========Musik finish===========

#===========Instagram start===========
            elif '.ig ' in msg.text.lower():
              if msg.from_ in Creator:
                try:
                    instagram = msg.text.lower().replace(".ig ","")
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
                    detail = "========INSTAGRAM INFO========\n"
                    details = "\n========INSTAGRAM INFO========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#===========Instagram finish===========


#==========Kerang ajaib start============
            elif "Apakah " in msg.text:
              if msg.from_ in Creator:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Ya","Tidak","Mungkin","Bacot","Gue capek ditanya terus"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Hari " in msg.text:
              if msg.from_ in Creator:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                


            elif "Berapa " in msg.text:
              if msg.from_ in Creator:
                apk = msg.text.replace("Berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Berapakah " in msg.text:
              if msg.from_ in Creator:
                apk = msg.text.replace("Berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "Kapan " in msg.text:
              if msg.from_ in Creator:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah","Tidak tau"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#==========Kerang ajaib finish============

#==========Youtube Start============
            elif ".Youtubesearch " in msg.text:
              if msg.from_ in Creator:
                query = msg.text.replace(".Youtubesearch ","")
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
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'


            elif '.Youtubelink ' in msg.text:
              if msg.from_ in Creator:
                  if msg.from_ in Creator:
                    try:
                        textToSearch = (msg.text).replace('.Youtubelink ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class':'yt-uix-tile-link'})
                        cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        cl.sendText(msg.to,"Tidak dapat mencarinya")
                    
                    
            elif '.Youtubevideo ' in msg.text:
              if msg.from_ in Creator:
                try:
                    textToSearch = (msg.text).replace('.Youtubevideo ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                    cl.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to, "Could not find it")   
#==========Youtube finish============

#==========Say Start============
            elif "Say-id " in msg.text:
              if msg.from_ in Creator:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
              if msg.from_ in Creator:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
              if msg.from_ in Creator:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#==========Say Finish============

#==========Welcome Start============
            elif ".welcome" in msg.text:
              if msg.from_ in Creator:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace(".welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#==========Welcome finish============

#==========Translate start============
            elif "Id@en" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO ENG]==\n" + "" + result + "\n\n==[SUKSES]==")


            elif "En@id" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM ENG]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
                
            
            elif "Id@jp" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO JPN]==\n" + "" + result + "\n\n==[SUKSES]==")
                
            
            elif "Jp@id" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM JPN]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")

            elif "Id@th" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO THA]==\n" + "" + result + "\n\n==[SUKSES]==")


            elif "Th@id" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM THA]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
  

            elif "Id@ar" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO ARG]==\n" + "" + result + "\n\n==[SUKSES]==")


            elif "Ar@id" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM AR]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")


            elif "Id@ko" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO KOR]==\n" + "" + result + "\n\n==[SUKSES]==")


            elif "Ko@id" in msg.text:
              if msg.from_ in Creator:
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
                cl.sendText(msg.to,"==[FROM KOR]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
#==========Translate finish============

#==============================================================   GROUP COMMAND   ==============================================================

#==========Katakan selamat datang start==========
            elif ".welcome" in msg.text:
              if msg.from_ in Creator:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace(".welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#==========Katakan selamat datang finish==========

#==========Invite Creator start==========
            elif "Invite creator" in msg.text:
                midd = "ua5f2cbc325816777be5ef529eb920c50"
                cl.inviteIntoGroup(msg.to,[midd])
#==========Invite Creator finish==========

#=========Recover Start===========
	    elif "Recover" in msg.text:
	      if msg.from_ in Creator:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
#=========Recover finish===========

#=========Group Creator start===========
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Buat Grup Ini")
#=========Group Creator finish===========

#=========Group info start===========
            elif msg.text == "Ginfo":
              if msg.from_ in Creator:
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
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
#=========Group info finish===========

#=========Group URL start===========
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
#=========Group URL finish===========

#=========Group list/group id start===========
            elif msg.text in ["Glist"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠❂➣ " + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╔═════════════════════════\n║          ◄GROUP LIST NvStar BOT►\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Group id"]:
              if msg.from_ in Creator:
                  gid = cl.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                  cl.sendText(msg.to,h)
#=========Group list/group id finish===========


#=========Picture group start===========
            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#=========Picture group finish===========

#=========Kick MID start===========
            elif "Kick: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick: ","")
                kicker = [ki,kk,kc]
                if midd not in admin:
                    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
                else:
                    cl.sendText(msg.to,"Tidak dapat kick admin BOT ini")
#=========Kick MID finish===========

#=========Invite MID start===========
            elif "Invite: " in msg.text:
              if msg.from_ in Creator:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                ki.findAndAddContactsByMid(midd)
                kk.findAndAddContactsByMid(midd)
                kc.findAndAddContactsByMid(midd)
                ks.findAndAddContactsByMid(midd)
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])
                cl.sendText(msg.to,"Pesan untuk admin./n gunakan invite bot ini hanya jika dalam keadaan terpaksa")
#=========Invite MID finish===========

#=========Invite Contact start===========
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    cl.sendText(msg.to,"Send Contact")
                    cl.sendText(msg.to,"Pesan untuk admin./n gunakan invite bot ini hanya jika dalam keadaan terpaksa")
#=========Invite Contact finish===========

#=========Member list  start===========
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════[LIST MEMBER]═════════"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════[LIST MEMBER]═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
#=========Member list start===========

#=========Get group image start===========
            elif "Getgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
#=========Get group image finish===========

#=========Get group url start===========
            elif "Urlgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
#=========Get group url finish===========

#==============================================================   CREATOR COMMAND   ==============================================================

#=========Admin add/remove start===========
            elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin NvStar BOT Berhasil Ditambahkan")
                            cl.sendText(msg.to,"Admin Power Dapat Menggunakan Command Khusus Untuk Mengatur BOT ini")
                        except:
                            pass
                print "[Command]Admin add executed"
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin NvStar BOT Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
#=========Admin add/remove finish===========

#=========Admin list start===========
            elif msg.text in ["Admin list","admin list","List admin","Adminlist"]:
              if msg.from_ in Creator:
                if admin == []:
                    cl.sendText(msg.to,"The Admin List Is Empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = "╔═════════════════════════\n║        ◄ADMIN NvStar BOT►\n╠═════════════════════════\n"
                    for mi_d in admin:
                        mc += "╠❂➣ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc + "╚═════════════════════════")
                    print "[Command]Admin List executed"

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~kazereborn")
		    cl.sendText(msg.to,"Broadcast Success")
#=========Admin list finish===========

#=========Join group by name start===========
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		gid = ki.getGroupIdsJoined()
		gid = kk.getGroupIdsJoined()
		gid = kc.getGroupIdsJoined()
		gid = ks.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
                            h = ki.getGroup(i).name
                            h = kk.getGroup(i).name
                            h = kc.getGroup(i).name
                            h = ks.getGroup(i).name
		            if h == ng:
		                random.choice(KAC).inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Membutuhkan izin creator")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
#=========Join group by name finish===========

#=========Leave group by name Start===========
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            cl.leaveGroup(i)
			    ki.leaveGroup(i)
			    kk.leaveGroup(i)
			    kc.leaveGroup(i)
			    ks.leaveGroup(i)
			    cl.sendText(msg.to,"Success Left ["+ h +"] group")
#=========Leave group by name finish===========

#=========Server info start===========
            elif msg.text.lower() == 'ifconfig':
                  if msg.from_ in Creator:
                      botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                  if msg.from_ in Creator:
                      botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                  if msg.from_ in Creator:
                      botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                  if msg.from_ in Creator:
                      botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#=========Server info finish===========

#=========Reboot or off start===========
            elif msg.text in ["Bot restart","Reboot"]:
                if msg.from_ in Creator:
                    cl.sendText(msg.to, "Bot Has Been Restarted...")
                    restart_program()
                    print "@Restart"

            elif msg.text in ["Turn off"]: 
                if msg.from_ in Creator:                
                    try:
                        import sys
                        sys.exit()
                    except:
                        pass 
#=========Reboot or off start===========

#==============================================================   ADMIN COMMAND   ==============================================================

#=========Ban mention start===========
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kc.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes BosQ")
                                except:
                                    cl.sendText(msg.to,"Error")
                            else:
                                cl.sendText(msg.to,"Tidak dapat banned sesama admin di BOT ini")
#=========Ban mention finish===========

#=========Ban contact start===========
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    ki.sendText(msg.to,"send contact")
#                else:
#                    msg.contentType = 13
#                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
#                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")    
#                    cl.sendMessage(msg)
#=========Ban contact finish===========

#=========Unban mention start===========
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kk.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Unban Berhasil")
                            except:
                                ki.sendText(msg.to,"Unban Berhasil")
#=========Unban mention finish===========

#=========Clear all bannad start===========
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"Daftar blacklist telah dibersihkan") 
#=========Clear all bannad start===========

#=========Banned list start===========
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#=========Banned list finish===========

#=========Banned list via ID start===========
            elif msg.text in ["Cek ban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        cocoa = ""
                        for mm in matched_list:
                            cocoa += mm + "\n"
                        cl.sendText(msg.to,cocoa + "")
#=========Banned list via ID finish===========

#=========Speed start===========
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "Progress...")
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))
#=========Speed finish===========

#=========Creator info start===========
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': WIB}
                cl.sendText(msg.to,"Hallo jika kalian memerlukan sesuatu\nSilahkan PM owner kami dibawah ini")
                cl.sendMessage(msg)
#=========Creator info finish===========


#=========Bot say hello start===========
            elif msg.text.lower() in ["hi","hai","halo","hallo","hello"]:
                    beb = "Hi Sayang 😘 " +cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    ks.sendText(msg.to,beb)
#=========Bot say hello finish===========

#=========Kill ban start===========
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
#=========Kill ban finish===========

#=========Remove Chat start===========
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        ks.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")      
#=========Remove Chat finish===========


            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")

            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")


            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass




    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
#def autolike():
#    for zx in range(0,500):
#      hasil = cl.activity(limit=500)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by ⭐⭐Koplaxs⭐⭐👈\n\n™SMULE VOICE FAMILY™")
#          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
#          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
#          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
#          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
#          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"=====Ready=====\n[★]Bot Protect For Group\n[★]\n[★]Selfbot in Your Account[★]\n- 1 Selfbot 1 Bot Assist\n- 1 Selfbot 2 Bot Assist\n- 1 Selfbot 3 Bot Assist\n- 1 Selfbot 4 Bot Assist\n- 1 Selfbot 5 Bot Assist\n\nMau Coba Atau Test Terlebih Dahulu Bisa\nMinat??? PM Id Line @hanavy1992\nLagu Promo Lho Kak\n===[★]One Piece Bot Protect[★]===")
#          print "Like"
#        except:
#          pass
#      else:
#          print "Already Liked"
#time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
#def likePost():
#    for zx in range(0,500):
#        hasil = cl.activity(limit=500)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#            if hasil['result']['posts'][zx]['userInfo']['mid'] in Creator:
#                try:
#                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ^One Piece Bot^\nStatus Boss udah Kami Like\nCreator Kami :\nHanavy Koplaxs")
#                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"=====Ready=====\n[★]Bot Protect For Group\n[★]\n[★]Selfbot in Your Account[★]\n- 1 Selfbot 1 Bot Assist\n- 1 Selfbot 2 Bot Assist\n- 1 Selfbot 3 Bot Assist\n- 1 Selfbot 4 Bot Assist\n- 1 Selfbot 5 Bot Assist\n\nMau Coba Atau Test Terlebih Dahulu Bisa\nMinat??? PM Id Line @hanavy1992\nLagu Promo Lho Kak\n===[★]One Piece Bot Protect[★]===")
#                    print "Like"
#                except:
#                    pass
#            else:
#                print "Status Sudah di Like Plak"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

try:
    response = urllib2.urlopen(request).read()
except SocketError as e:
    if e.errno != errno.ECONNRESET:
        raise # Not error we are looking for
    pass # Handle error here.

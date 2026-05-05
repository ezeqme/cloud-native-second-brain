---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security"]
speakers: ["Omri Gazitt", "Aserto"]
sched_url: https://kccncna2024.sched.com/event/1i7kR/authzen-the-openid-connect-for-authorization-omri-gazitt-aserto
youtube_search_url: https://www.youtube.com/results?search_query=AuthZEN%3A+The+%E2%80%9COpenID+Connect%E2%80%9D+for+Authorization+CNCF+KubeCon+2024
slides: []
status: parsed
---

# AuthZEN: The “OpenID Connect” for Authorization - Omri Gazitt, Aserto

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Omri Gazitt, Aserto
- Schedule: https://kccncna2024.sched.com/event/1i7kR/authzen-the-openid-connect-for-authorization-omri-gazitt-aserto
- Busca YouTube: https://www.youtube.com/results?search_query=AuthZEN%3A+The+%E2%80%9COpenID+Connect%E2%80%9D+for+Authorization+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre AuthZEN: The “OpenID Connect” for Authorization.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kR/authzen-the-openid-connect-for-authorization-omri-gazitt-aserto
- YouTube search: https://www.youtube.com/results?search_query=AuthZEN%3A+The+%E2%80%9COpenID+Connect%E2%80%9D+for+Authorization+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MTAXC0ZaXcE
- YouTube title: AuthZEN: The “OpenID Connect” for Authorization - Omri Gazitt, Aserto
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/authzen-the-openid-connect-for-authorization/MTAXC0ZaXcE.txt
- Transcript chars: 34030
- Keywords: authorization, access, policy, actually, to-dos, application, google, document, around, source, authentication, standards, answer, resource, decision, called, little, control

### Resumo baseado na transcript

thank you my name is Omar gazit I am the co-founder and CEO of acerto which is an authorization company but I'm also wearing another hat today I am uh the co-chair of the newest open ID Foundation working group called ozen and so I'm here to talk to you about the work that we're doing in oen around standardizing authorization our goal is no less than becoming the open ID connect of authorization who knows what ID connect is pretty much everyone excellent a little bit by myself before

### Excerpt da transcript

thank you my name is Omar gazit I am the co-founder and CEO of acerto which is an authorization company but I'm also wearing another hat today I am uh the co-chair of the newest open ID Foundation working group called ozen and so I'm here to talk to you about the work that we're doing in oen around standardizing authorization our goal is no less than becoming the open ID connect of authorization who knows what ID connect is pretty much everyone excellent a little bit by myself before we start I've been doing software for Developers for well over 30 years now um I uh helped start theet project of Microsoft I was also one of the co-founders of azure uh the general manager for what became Azure active directory so have a lot of roots in the identity and access space about 12 years ago I started working on open source uh including openstack and Cloud Foundry later on Docker and kubernetes uh most recently puppet uh I love startups Aero is my third startup and when I'm not start uping I'm skiing uh although as I mentioned yesterday in my talk I'm really um chafed at the fact that the slopes are opening a week from Friday so I could not combine this with with a ski trip so who knows the difference between authentication and authorization everyone all right I won't Bel labor this authentication did the user prove that they are who they say they are back when I started in this industry industry was user IDs and passwords now it's magic links and uh pass keys and Biometrics but the process is all the same authorization what can they do in the context of this application who knows some of these standards that I've uh put up on here saml 20 years old now um ooth 2 16 years old open ID connect as we said 11 years old these are mature standards in the space and you have a set of mature developer services that Implement these standards so that no one needs to go build login authentication on their own if they don't have to right you have ozero and you have Cognito and you have Azure active directory entra ID now so on and so forth uh to help you with that as opposed to doing some undifferentiated heavy lifting so this is a solved problem authorization not solved who can tell me like can anybody shout a name of an authorization standard that you know about Zach zacho all right who else MAA yes um there are two so uh I think uh there are about 200 people in the audience 150 that's 2% of you that um know about authorization standards so not very well uh known uh certainly

---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Jesse Sanford", "Greg Haynes", "Autodesk"]
sched_url: https://kccnceu2024.sched.com/event/1YeRp/rapid-idp-capability-development-and-automated-testing-at-autodesk-jesse-sanford-greg-haynes-autodesk
youtube_search_url: https://www.youtube.com/results?search_query=Rapid+IDP+Capability+Development+and+Automated+Testing+at+Autodesk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Rapid IDP Capability Development and Automated Testing at Autodesk - Jesse Sanford & Greg Haynes, Autodesk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Jesse Sanford, Greg Haynes, Autodesk
- Schedule: https://kccnceu2024.sched.com/event/1YeRp/rapid-idp-capability-development-and-automated-testing-at-autodesk-jesse-sanford-greg-haynes-autodesk
- Busca YouTube: https://www.youtube.com/results?search_query=Rapid+IDP+Capability+Development+and+Automated+Testing+at+Autodesk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Rapid IDP Capability Development and Automated Testing at Autodesk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRp/rapid-idp-capability-development-and-automated-testing-at-autodesk-jesse-sanford-greg-haynes-autodesk
- YouTube search: https://www.youtube.com/results?search_query=Rapid+IDP+Capability+Development+and+Automated+Testing+at+Autodesk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=x_cTXvRgwdA
- YouTube title: Rapid IDP Capability Development and Automated Testing at Autodesk - Jesse Sanford & Greg Haynes
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/rapid-idp-capability-development-and-automated-testing-at-autodesk/x_cTXvRgwdA.txt
- Transcript chars: 35576
- Keywords: actually, backstage, platform, development, argo, source, builder, developer, basically, template, software, tooling, create, working, reference, together, github, experience

### Resumo baseado na transcript

thanks for joining us everybody um hope we're all having a great cucon and almost the end I think two more talks after this so thanks for joining us at the end of the conference here I hope we're all having a great time so Jesse and I are here to talk to you today about rapid IDP development um so this topic is a topic that has a lot of interest right now it's something that we're very passionate about and more not only that we've been working on

### Excerpt da transcript

thanks for joining us everybody um hope we're all having a great cucon and almost the end I think two more talks after this so thanks for joining us at the end of the conference here I hope we're all having a great time so Jesse and I are here to talk to you today about rapid IDP development um so this topic is a topic that has a lot of interest right now it's something that we're very passionate about and more not only that we've been working on a lot of Open Source tools and technologies that we'd like to share with you today so one in the morning interesting things about this talk is at the end you'll see some QR codes where you can find all the source code for our demos and the tools that we we've developed here but first I'd like to introduce ourselves so Jesse you want to take it off sure got over here hi everybody and are these hot okay there we go all right yeah I'm Jesse Sanford I'm a software architect at Autodesk I work on our developer enablement team which handles our internal develop developer platform um and I when I'm not doing that I like to work on software supply chain security so you might see me speak over there sometimes too um and when I'm not working I like to sail and spend time outdoors with my daughters thanks Jesse um and I'm Greg Hayes I'm also a software architect at Autodesk focused on our Cloud software delivery platform uh most of my background's in open source Cloud software so I'm fairly passionate about it and I guess since we're talking Hobbies my mine what I'm not working is lately snowboarding a lot with my two my two kids so what are we here to talk about um first I'm going to start out a bit with the why you know like what what are challenges I've been facing at AES and I'm I'm going to try to convince you all based upon these challenges we've had what is the value in creating some the tooling and a reference the tooling to create internal reference developer platforms or idps after some of that history and context we'll start to talk about the tools we created and open sourced so these tools really help accelerate the development of our internal developer platform and I'm hopeful that they can be useful for you all as well and then finally Jesse has an awesome demo he's put together that he's going to show you all play to the demo gods that everything goes smoothly but um his demo it's really interesting and it's basically how you can use these tools to do this rapid IDP development so how did we get here so at at

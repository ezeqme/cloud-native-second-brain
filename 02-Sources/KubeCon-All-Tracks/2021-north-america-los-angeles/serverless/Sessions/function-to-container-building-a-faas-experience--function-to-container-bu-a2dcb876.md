---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Serverless"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Evan Anderson", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV3n/function-to-container-building-a-faas-experience-evan-anderson-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Function+to+Container+-+Building+a+FaaS+Experience+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Function to Container - Building a FaaS Experience - Evan Anderson, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Serverless]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United States / Los Angeles
- Speakers: Evan Anderson, VMware
- Schedule: https://kccncna2021.sched.com/event/lV3n/function-to-container-building-a-faas-experience-evan-anderson-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Function+to+Container+-+Building+a+FaaS+Experience+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Function to Container - Building a FaaS Experience.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3n/function-to-container-building-a-faas-experience-evan-anderson-vmware
- YouTube search: https://www.youtube.com/results?search_query=Function+to+Container+-+Building+a+FaaS+Experience+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y78WRqfsmG8
- YouTube title: Function to Container - Building a FaaS Experience - Evan Anderson, VMware
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/function-to-container-building-a-faas-experience/Y78WRqfsmG8.txt
- Transcript chars: 26567
- Keywords: actually, function, python, container, docker, little, developer, experience, language, programming, environment, having, spring, figure, started, around, package, native

### Resumo baseado na transcript

thank you thank you and yeah i'm happy to discuss any of this stuff um catch me outside my twitter's at the end um there's a couple calls to action at the end too so um you know the end of the talk hopefully i'll have motivated you to do some of that stuff but we're going to start with a little trip down memory lane so this is a lot about application developers folks whose job it is wow that's a little out can we get down just a

### Excerpt da transcript

thank you thank you and yeah i'm happy to discuss any of this stuff um catch me outside my twitter's at the end um there's a couple calls to action at the end too so um you know the end of the talk hopefully i'll have motivated you to do some of that stuff but we're going to start with a little trip down memory lane so this is a lot about application developers folks whose job it is wow that's a little out can we get down just a tiny bit okay um folks who are mostly not worried about the stuff we're doing here today they're mostly worried about solving business problems and producing business value so um looks like it's a little loud still i've been told i'm out loud thank you um so when everything started you know you started with maine and we experiment with functional languages and object-oriented languages along the way we figured out different ways to organize our code and so we've been doing this for 40 years 50 years so if you were in the late 1970s and you were going to build well you didn't build a web service then but a network service you got all of this setup code to write before you actually got around to doing anything interesting and then it was kind of painful to do interesting things because you had to worry about like buffer overflows and yeah maybe c isn't the greatest language nowadays but in the 80s we figured out hey we can make this way easier if we get someone else to open up that socket for us and we just connect it to standard and standard out and so that's what inetd does and you just need to write your stuff in there and pass it to standard and stand it out and so your network programming gets a lot simpler here's where i made my introduction to programming cgi bin did the same thing for http so you put your perl script on a path and you got all of your arguments like all of your http headers passed in as environment variables you got the body passed in as the request body and you spat back some htm some hdp headers and then a body um and i think that even works i haven't tried it um but uh but that made things a lot easier for writing programs and so lots of people got started writing web apps with this kind of stuff in the 2000 rails came along and the code doesn't look a lot different except if we look at that middle block there where it says rails applications routes draw do we've moved mapping all those http paths from files in the file system to something that's under your programming control so you can actually choose wit

---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Open Interfaces + Interoperability"
themes: ["Runtime Containers"]
speakers: ["Mauricio Salatino", "Diagrid", "Adrian Cole", "Tetrate"]
sched_url: https://kccnceu2023.sched.com/event/1HyW0/safe-dynamic-middleware-with-dapr-and-webassembly-mauricio-salatino-diagrid-adrian-cole-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=Safe%2C+Dynamic+Middleware+with+Dapr+and+WebAssembly+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Safe, Dynamic Middleware with Dapr and WebAssembly - Mauricio Salatino, Diagrid & Adrian Cole, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mauricio Salatino, Diagrid, Adrian Cole, Tetrate
- Schedule: https://kccnceu2023.sched.com/event/1HyW0/safe-dynamic-middleware-with-dapr-and-webassembly-mauricio-salatino-diagrid-adrian-cole-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=Safe%2C+Dynamic+Middleware+with+Dapr+and+WebAssembly+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Safe, Dynamic Middleware with Dapr and WebAssembly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyW0/safe-dynamic-middleware-with-dapr-and-webassembly-mauricio-salatino-diagrid-adrian-cole-tetrate
- YouTube search: https://www.youtube.com/results?search_query=Safe%2C+Dynamic+Middleware+with+Dapr+and+WebAssembly+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DXW9kB0NsUY
- YouTube title: Safe, Dynamic Middleware with Dapr and WebAssembly - Mauricio Salatino, Diagrid & Adrian Cole
- Match score: 0.801
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/safe-dynamic-middleware-with-dapr-and-webassembly/DXW9kB0NsUY.txt
- Transcript chars: 33857
- Keywords: application, dapper, webassembly, actually, basically, component, filter, applications, configuration, components, running, without, writing, sidecar, middleware, write, process, little

### Resumo baseado na transcript

so uh who are we well there's three of us I swear uh one of them's a ghost in the show uh so uh Long die actually uh led a lot of the work that we're talking about today but he was in uh Shanghai and not able to actually get out of here um so we have a video segment but but uh long as an excellent part of this process and we want to you know acknowledge that as we go along um I'm Adrian um and I

### Excerpt da transcript

so uh who are we well there's three of us I swear uh one of them's a ghost in the show uh so uh Long die actually uh led a lot of the work that we're talking about today but he was in uh Shanghai and not able to actually get out of here um so we have a video segment but but uh long as an excellent part of this process and we want to you know acknowledge that as we go along um I'm Adrian um and I work at tetrate and I work on the webassembly runtime call was Zero which is we're just threatening to go and um I got acclimated to to adapter much more so through through this work so I'm sort of like a community contributor and yes Mauricio Mauricio I work for diabet and I think we have a couple of slides like introducing right yes yeah that's that's you that's your Twitter account that's me yeah good so uh yep uh I'm code from the Crypt um and so if you want to follow follow those things yeah promise that it meets its name definitely and uh yeah and if you're interested in these topics yeah I'm at Salah Twitter as well I work for this company called diagram we help people run Dapper in production and you know in multiple clouds and I'm writing this book uh the title platform engineering kubernetes where I'm covering I like these topics on how you put different projects together and how you expand platforms is kind of like the topic of today's session uh that's a QR for the book and down there it's my name with 40 that's my age unfortunately but it's also a 40 discount code if you're interested in that I'm just writing your book I I'm trying to you know I'm trying to find like a positive angle of the 40 thing but let's let's do it so this is the this is what we're going to be talking about uh today uh we are going to start like with Dapper that's showing it in action uh how many developers do we have here in the room yeah that's a good 30 I would say maybe uh and then we are going to talk a little bit about how we are kind of combining Dapper and we have assembly together and then we're just going to see another demo showing that exactly I think that what we are showing here is just the starting points for collaborations and there are tons of other things that we can be doing so if you don't know anything about upper adapter it's a cncf project it's a distributed application runtime and I will not spend so much time discussing about what diaper is I wanted to show you in action but you need to know two things about upper it's thriving on the cncf community it's

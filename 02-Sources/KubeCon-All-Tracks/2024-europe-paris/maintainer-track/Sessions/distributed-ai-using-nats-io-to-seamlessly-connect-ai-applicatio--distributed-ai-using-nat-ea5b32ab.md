---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Tomasz Pietrek", "Jeremy Saenz", "Synadia"]
sched_url: https://kccnceu2024.sched.com/event/1YhgF/distributed-ai-using-natsio-to-seamlessly-connect-ai-applications-from-cloud-to-edge-tomasz-pietrek-jeremy-saenz-synadia
youtube_search_url: https://www.youtube.com/results?search_query=Distributed+AI%3A+Using+NATS.Io+to+Seamlessly+Connect+AI+Applications+from+Cloud+to+Edge+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Distributed AI: Using NATS.Io to Seamlessly Connect AI Applications from Cloud to Edge - Tomasz Pietrek & Jeremy Saenz, Synadia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Tomasz Pietrek, Jeremy Saenz, Synadia
- Schedule: https://kccnceu2024.sched.com/event/1YhgF/distributed-ai-using-natsio-to-seamlessly-connect-ai-applications-from-cloud-to-edge-tomasz-pietrek-jeremy-saenz-synadia
- Busca YouTube: https://www.youtube.com/results?search_query=Distributed+AI%3A+Using+NATS.Io+to+Seamlessly+Connect+AI+Applications+from+Cloud+to+Edge+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Distributed AI: Using NATS.Io to Seamlessly Connect AI Applications from Cloud to Edge.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhgF/distributed-ai-using-natsio-to-seamlessly-connect-ai-applications-from-cloud-to-edge-tomasz-pietrek-jeremy-saenz-synadia
- YouTube search: https://www.youtube.com/results?search_query=Distributed+AI%3A+Using+NATS.Io+to+Seamlessly+Connect+AI+Applications+from+Cloud+to+Edge+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZcgFgb8dLOw
- YouTube title: Distributed AI: Using NATS.Io to Seamlessly Connect AI Applications... Tomasz Pietrek & Jeremy Saenz
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/distributed-ai-using-nats-io-to-seamlessly-connect-ai-applications-fro/ZcgFgb8dLOw.txt
- Transcript chars: 34429
- Keywords: actually, little, server, everybody, running, stream, configuration, request, distributed, connect, metrics, pretty, object, applications, technology, jeremy, awesome, whatever

### Resumo baseado na transcript

excellent hello everybody come on in come on in we have so much stuff to cover today this is actually going to be a really fun time um oh do we have T-shirts by the way we have T-shirts oh my gosh okay we're going to have a lot of fun today but we have a ton to cover thanks for joining us on this talk today we're going to be talking about AI at the edge um and using this really fun technology called gats to do it and greater than okay cool these are all metrics that are being emitted by all of you and I was able to just tap into it because it's something that's available in Nets not only that but I could take this and I could actually put into a jet stream an actual stream and save that data with all different parameters into how I want to do that it's actually very easy to do I could just say Nat's uh stream create um metrics and I'm just going to say you subjects thank you so I could type this in apparently I don't know what how plurals work and so now we have a new stream that shows up here for metrics and we already have 101 messages and those are all metrics that are emitted nickname this going to print out somebody's nickname here um there we go Problem Child excellent so I I found the best nickname right off of the bat but it's going to it's going to continue to um it's going to continue to use uh

### Excerpt da transcript

excellent hello everybody come on in come on in we have so much stuff to cover today this is actually going to be a really fun time um oh do we have T-shirts by the way we have T-shirts oh my gosh okay we're going to have a lot of fun today but we have a ton to cover thanks for joining us on this talk today we're going to be talking about AI at the edge um and using this really fun technology called gats to do it and um this is also going to be really interactive so get your like laptops ready this is going to be like one of the talks where you can actually take your laptop out and nobody's going to P you for it um take your laptops out take your phones out um we're going to be having a great time so before we begin scan this QR code or even better on your laptop just go to this URL really quick fill out a quick survey this is not just for me to collect information about you but it's actually going to be part of the interactive demo throughout this time so be sure to do that you can get a chance to win a T-shirt and also you'll just have a lot more fun during this talk um all right scan it I'll give you guys a few minutes to do so um and I guess before we do that we can go through our slides but I'll give you some time to scan it and I'll intro myself hi my name is Jeremy I work for Cadia we are the maintainers of the Nats iio project where many of us are maintainers at the Nats IO project um which is a cncf based project and I've been working in all kinds of Industries um but I get to talk about how cool Nats is now um which is super super fun working in distributed systems is pretty awesome and toas I'll just let you intro yourself know yeah hey everybody I'm toas I'm running the OSS team for Sadia so the maintainers of uh of the technology uh beyond that I'm coding go in rust or whatever is needed recently that's Swift which will come back later H in the past I work in different industries spanning from fintech Telco e-commerce and and whatnot across all the possible ones awesome and so before we get into the slides let's go ahead and check out um how things are going over here in uh this app so it looks like we have people filling stuff out we have folks who are working in um technology which I guess makes sense um and folks are interested in stuff like event streaming microservices it's about like a pretty even split which is great we're going to try to address many of these things today um and we have a mix of people who are newbies and also a good c

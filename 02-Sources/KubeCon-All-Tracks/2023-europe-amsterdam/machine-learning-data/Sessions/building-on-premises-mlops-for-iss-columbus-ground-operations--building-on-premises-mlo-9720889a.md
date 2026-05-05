---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data"]
speakers: ["Samo Turk", "Christian Geier", "JUST ADD AI GmbH"]
sched_url: https://kccnceu2023.sched.com/event/1HyXV/building-on-premises-mlops-for-iss-columbus-ground-operations-samo-turk-christian-geier-just-add-ai-gmbh
youtube_search_url: https://www.youtube.com/results?search_query=Building+on-Premises+MLOps+for+ISS+Columbus+Ground+Operations+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building on-Premises MLOps for ISS Columbus Ground Operations - Samo Turk & Christian Geier, JUST ADD AI GmbH

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Samo Turk, Christian Geier, JUST ADD AI GmbH
- Schedule: https://kccnceu2023.sched.com/event/1HyXV/building-on-premises-mlops-for-iss-columbus-ground-operations-samo-turk-christian-geier-just-add-ai-gmbh
- Busca YouTube: https://www.youtube.com/results?search_query=Building+on-Premises+MLOps+for+ISS+Columbus+Ground+Operations+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building on-Premises MLOps for ISS Columbus Ground Operations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXV/building-on-premises-mlops-for-iss-columbus-ground-operations-samo-turk-christian-geier-just-add-ai-gmbh
- YouTube search: https://www.youtube.com/results?search_query=Building+on-Premises+MLOps+for+ISS+Columbus+Ground+Operations+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g3a-NJwGUvY
- YouTube title: Building on-Premises MLOps for ISS Columbus Ground Operations - Samo Turk & Christian Geier
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-on-premises-mlops-for-iss-columbus-ground-operations/g3a-NJwGUvY.txt
- Transcript chars: 26041
- Keywords: actually, storage, kubeflow, quickly, grafana, platform, especially, obviously, decided, everything, cluster, mentioned, important, deployments, operator, pretty, perhaps, station

### Resumo baseado na transcript

hello welcome to our talk on ML Ops um for ground operations of the ISS we are really excited to be here especially excited that so many of you made it to the stock at such a late hour um aren't partying yet down in the exhibition Hall before we start talking about ml Ops we'll give you a brief introduction about ourselves and how we got here I'll start so my title nowadays is data scientist but I haven't done any data scientisting in quite some time instead I've

### Excerpt da transcript

hello welcome to our talk on ML Ops um for ground operations of the ISS we are really excited to be here especially excited that so many of you made it to the stock at such a late hour um aren't partying yet down in the exhibition Hall before we start talking about ml Ops we'll give you a brief introduction about ourselves and how we got here I'll start so my title nowadays is data scientist but I haven't done any data scientisting in quite some time instead I've been a data engineer data architect something like that so basically building all of what we're going to talk about as part of a larger team I used to be a physicist and did a PhD there got a lot into data analytics there also like running bigger clusters and so on it's been a data science consultant for some time after this that's where I picked up wearing jacket like this physicists don't look there like that usually but I'm a long time Unix nerd which really helped me out with this because I actually had no previous exposure to kubernetes at all before obviously I knew what it was but had never really touched it um but without that 20 years of Unix experience that would have been a much harder Journey hey uh I'm Samo a similar role as Christian slightly different background so my background is in life science so I have a PhD in computer aided drug design so I spent quite some years working in Pharma and after that in Consulting before joining this company uh also we have Decades of experience with working with open source and and Linux and before embarking on this project I had some experience with kubernetes but that only from convenience of the cloud so this talk will be about we will just give you a high level overview of the use case but we'll then mostly focus on our approach towards designing and building these MLS mlops platform and obviously on-prem without the cloud we'll talk about major components we used and and how we decided for them uh we'll touch automation resistance storage networking logging monitoring and then finally we'll give you some tips and tricks and some useful tools that we discovered during this journey so what we won't be talking about is any you know kubeflow details running pipelines ml jobs things like that uh we also won't go into any details about autonomy detection root cause analysis and other algorithms we are developing and also fortunately we don't have time to to go into any details about International Space Station so the work here is uh sponsored as p

---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability"]
speakers: ["Andreas Grabner", "Dynatrace"]
sched_url: https://kccnceu2022.sched.com/event/ytwU/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-prometheus-and-keptn-andreas-grabner-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Thank+you+Keptn+Obvious%21+Making+SLOs+observable+with+Prometheus+and+Keptn+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Lightning Talk: Thank you Keptn Obvious! Making SLOs observable with Prometheus and Keptn - Andreas Grabner, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Andreas Grabner, Dynatrace
- Schedule: https://kccnceu2022.sched.com/event/ytwU/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-prometheus-and-keptn-andreas-grabner-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Thank+you+Keptn+Obvious%21+Making+SLOs+observable+with+Prometheus+and+Keptn+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Lightning Talk: Thank you Keptn Obvious! Making SLOs observable with Prometheus and Keptn.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytwU/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-prometheus-and-keptn-andreas-grabner-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Thank+you+Keptn+Obvious%21+Making+SLOs+observable+with+Prometheus+and+Keptn+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5NDozsGMWIg
- YouTube title: Lightning Talk: Thank you Keptn Obvious! Making SLOs observable with Prometheus a... Andreas Grabner
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-pro/5NDozsGMWIg.txt
- Transcript chars: 5882
- Keywords: captain, observability, prometheus, actually, making, trying, decisions, desired, orchestration, obvious, actionable, native, connect, always, observable, kubecon, slides, obviously

### Resumo baseado na transcript

all right well thanks first of all for being so dedicated to kubecon it's 5 30 on a beautiful day and you're here and not at the bars so thank you so much i also want to say thank you to olek he was supposed to give this talk but unfortunately he had to travel and leave early so i'll do my best to give him justice but the great slides that you see are actually from him so if you ever see all the ghana chefs then give him

### Excerpt da transcript

all right well thanks first of all for being so dedicated to kubecon it's 5 30 on a beautiful day and you're here and not at the bars so thank you so much i also want to say thank you to olek he was supposed to give this talk but unfortunately he had to travel and leave early so i'll do my best to give him justice but the great slides that you see are actually from him so if you ever see all the ghana chefs then give him some kudos talk today thank you captain obvious making observability actionable with prometheus and captain obviously i try to make it obvious i really like captain um my name is andy gregner i work for dynatrace during the day but i'm also a captain maintainer and a contributor and i really like to show you what we are doing with captain if you think captain if you heard about captain you think captain is yet another cicd tool and it's a if this standpoint is told that hopefully i prove you wrong because i want to give you a little different perspective on captain captain has also changed over the last couple of years but if you want to get shirts or heads we also have a booth at the pavilion so check us out tomorrow but let me first get into my talk i talk about observability making observability actionable and when i talk up and think about observability i think about essays sovs are using observability data to keep systems reliable and resilient but you may say well one does not simply do a sre well i counter i think actually captain makes it pretty simple this is a post from tarash he is a performance engineer at facebook and when he saw that captain two years ago when we were still at the early stages you already saw we are trying to bring the srv core principles to the cloud native community letting observability that you pull out from prometheus or any other observability frame that she had using this to drive those actions that actually keep the system reliable um so first of all let me get started on what problem we really want to solve we all know that modern cloud native systems are no longer simple you have a lot of different tools and you need to connect them in one way or the other which means you have to build a lot of point-to-point integrations and trying to put in also your ability to make better decisions i'm pretty sure some of these tools are familiar the question is how can you make better informed decisions if you don't have visibility well fortunately we obviously talk a lot about observability in this conference i

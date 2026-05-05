---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["Observability"]
speakers: ["Michael Beemer", "Johannes Bräuer", "Dynatrace"]
sched_url: https://kccncna2022.sched.com/event/182FY/hands-off-features-releases-with-keptn-openfeature-and-opentelemetry-michael-beemer-johannes-brauer-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Hands-Off+Features+Releases+With+Keptn%2C+OpenFeature%2C+And+OpenTelemetry+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Hands-Off Features Releases With Keptn, OpenFeature, And OpenTelemetry - Michael Beemer & Johannes Bräuer, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Observability]]
- País/cidade: United States / Detroit
- Speakers: Michael Beemer, Johannes Bräuer, Dynatrace
- Schedule: https://kccncna2022.sched.com/event/182FY/hands-off-features-releases-with-keptn-openfeature-and-opentelemetry-michael-beemer-johannes-brauer-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Hands-Off+Features+Releases+With+Keptn%2C+OpenFeature%2C+And+OpenTelemetry+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Hands-Off Features Releases With Keptn, OpenFeature, And OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182FY/hands-off-features-releases-with-keptn-openfeature-and-opentelemetry-michael-beemer-johannes-brauer-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Hands-Off+Features+Releases+With+Keptn%2C+OpenFeature%2C+And+OpenTelemetry+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tOFI49bJkxA
- YouTube title: Hands-Off Features Releases With Keptn, OpenFeature, And Open... - Michael Beemer & Johannes Bräuer
- Match score: 0.903
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/hands-off-features-releases-with-keptn-openfeature-and-opentelemetry/tOFI49bJkxA.txt
- Transcript chars: 22345
- Keywords: feature, captain, basically, actually, process, production, environment, deployment, configuration, tooling, everything, staging, important, flagging, delivery, everyone, release, interesting

### Resumo baseado na transcript

we are super excited about our talk with we Amin Mike Beamer who is maintain our open feature and myself Johannes poya open source project why we are excited because today we want to bring together open feature Captain as well as open Telemetry in order to set up a releasing environment that allows us to release features in production without or in a very safe manner for our talk we have prepared a couple of sections Mike is going on to explain why it's important to have feature flagging

### Excerpt da transcript

we are super excited about our talk with we Amin Mike Beamer who is maintain our open feature and myself Johannes poya open source project why we are excited because today we want to bring together open feature Captain as well as open Telemetry in order to set up a releasing environment that allows us to release features in production without or in a very safe manner for our talk we have prepared a couple of sections Mike is going on to explain why it's important to have feature flagging adults afterwards he is presenting more details on open and then I will jump in and I will talk about Captain in the demo we are then bringing together Captain open feature and open Telemetry to release a new feature in the hands-off manner and finally we will then do a recap all right Mike let's get started all right thanks Johannes yeah so just a quick introduction to feature flag um basically it's a software technique that allows you to modify system Behavior Uh without requiring a redeployment and so it's really powerful it's used in a lot of ways very commonly it's used for like as a release toggle so you can put new functionality behind a feature flag and then enable it when you're ready you can use it for experimentation so a b testing or ABN testing where you would run experiment collect data analyze the results and then choose the best of the options uh you could also use it as an Ops toggle and so that's another way to look at feature Flags typically you would think of a feature flag is something that you would add your code you would use it until it's you know on or in a stable State and then remove it and Ops toggle would actually be used for basically the life of the project and you would use that in situations where you need to disable some kind of behavior to maybe save your system some load or if another third party service is down you can basically use that in operation mode and the last one is like a context aware toggle that's something that's going to be really important for this demo today and that's basically where you can pass in different contextual information like what users logged in what their Geo is or anything like that and then you can make decisions based on that metadata uh one way to do that or one of the big benefits of feature uh uh is basically you're decoupling your feature releases from a deployment so if you think you're writing your software you're doing your deployment you're sending it out to production traditionally that's basica

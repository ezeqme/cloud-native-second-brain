---
type: session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: Observability
sched_url: https://kccnceu2022.sched.com/event/ytwU/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-prometheus-and-keptn-andreas-grabner-dynatrace
youtube_url: https://www.youtube.com/watch?v=5NDozsGMWIg
youtube_id: 5NDozsGMWIg
video_match_score: 0.992
speakers: ["Andreas Grabner", "Dynatrace"]
topics: ["Metrics", "Tracing", "SLOs"]
slides: ["https://hosted-files.sched.co/kccnceu2022/53/KubeCon2022_LT4_GRABNER_Thank%20you%20Keptn%20Obvious.pptx"]
status: transcript-downloaded
---

# Lightning Talk: Thank you Keptn Obvious! Making SLOs observable with Prometheus and Keptn - Andreas Grabner, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- País/cidade: Spain / Valencia
- Ano: 2022
- Trilha/tema: Observability
- Tópicos: [[Metrics]], [[Tracing]], [[SLOs]]
- Speakers: Andreas Grabner, Dynatrace
- Schedule: https://kccnceu2022.sched.com/event/ytwU/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-prometheus-and-keptn-andreas-grabner-dynatrace
- YouTube: https://www.youtube.com/watch?v=5NDozsGMWIg

## Resumo

This talk shows how to not only collect metrics and provide application monitoring using Prometheus, but to also make them visible as SLOs and then act on them in a fully automated and cloud native way. Click here to view captioning/translation in the MeetingPlay platform!

## Descrição oficial

This talk shows how to not only collect metrics and provide application monitoring using Prometheus, but to also make them visible as SLOs and then act on them in a fully automated and cloud native way.

Click here to view captioning/translation in the MeetingPlay platform!

## Transcript

all right well thanks first of all for being so dedicated to kubecon it's 5 30 on a beautiful day and you're here and not at the bars so thank you so much i also want to say thank you to olek he was supposed to give this talk but unfortunately he had to travel and leave early so i'll do my best to give him justice but the great slides that you see are actually from him so if you ever see all the ghana chefs then give him some kudos talk today thank you captain obvious making observability actionable with prometheus and captain obviously i try to make it obvious i really like captain um my name is andy gregner i work for dynatrace during the day but i'm also a captain maintainer and a contributor and i really like to show you what we are doing with captain if you think captain if you heard about captain you think captain is yet another cicd tool and it's a if this standpoint is told that hopefully i prove you wrong because i want to give you a little different perspective on captain captain has also changed over the last couple of years but if you want to get shirts or heads we also have a booth at the pavilion so check us out tomorrow but let me first get into my talk i talk about observability making observability actionable and when i talk up and think about observability i think about essays sovs are using observability data to keep systems reliable and resilient but you may say well one does not simply do a sre well i counter i think actually captain makes it pretty simple this is a post from tarash he is a performance engineer at facebook and when he saw that captain two years ago when we were still at the early stages you already saw we are trying to bring the srv core principles to the cloud native community letting observability that you pull out from prometheus or any other observability frame that she had using this to drive those actions that actually keep the system reliable um so first of all let me get started on what problem we really want to solve we all know that modern cloud native systems are no longer simple you have a lot of different tools and you need to connect them in one way or the other which means you have to build a lot of point-to-point integrations and trying to put in also your ability to make better decisions i'm pretty sure some of these tools are familiar the question is how can you make better informed decisions if you don't have visibility well fortunately we obviously talk a lot about observability in this conference i also want to give a shout out to henrik in case you have not seen his phenomenal youtube channel it's called is it observable check it out he is looking at new frameworks in the space all the time and he gives his perspectives he also creates tutorials so check it out the point is observability is a must because if we don't have observability we cannot make good decisions we don't even know if the system is broken the problem is right observability is not easy if you know that you have a big landscape of tools and you don't really know how you actually get data out of this well fortunately again we have movements where we are trying to figure out how to standardize mobs ability i don't need to remind you about some of these great products or frameworks and projects here that are really trying to make it easier for us to get insights prometheus is one of them right i think with hunt and again this is if you like these slides ovec is the one to put them together i really like it right sauron's either prometheus i will give you all the visibility and what happens in your environment what we want to bring to the table if you have data then we as captain make it actionable if you have a desired state based on the data the system should be helping healthy it should be up and running it should be performing in a certain way we can act on this data to always keep the system in that interstate that you expect from your system based on your stability data so in other words captain is an observability driven orchestration engine for your cloud native apps what this means in again another cool slide from oleg one platform to orchestrate them all i hope i have some golden ring fans in here at least uh captain has been around for a while we are a cnc at sandbox project right now very close together reaching incubation what's really important is that orchestration and observability drifting orchestration is at the core and what this means is if i come back to the slide that i had earlier the clicker works as expected somebody needs to observe the signal here there we go all right one option that you have you can build orchestration yourself you can connect all of these tools but what we try to do is i just click here instead of you having to connect all of these tools and making decisions on what to do next captain's control plane reaches out to your observability platform and based on how the state of your system is then all the right tools to actually bring the system back to its healthy state so at the core of captain we have slo service level objectives you define the desired state of what your system you expect the system to be and then we orchestrate the tool to bring the system always back to the desired state but uh captain has a really cool rest api we are standardizing on cloud events and we are in the cdf events spec and i see them out of time what i would like you to know is if you have an app it's instrumented with open telemetry you get some data we can act on it to bring the system always back to its desired based on your observability captain is extendable there's a lot of stuff that we have out there check out nana's video if you know nana she did a a video on captain learn more about cabinet kubecon which means please meet us at the pavilion i am there and some others tomorrow thursday and friday thank you [Applause]

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytwU/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-prometheus-and-keptn-andreas-grabner-dynatrace
- Vídeo no YouTube: https://www.youtube.com/watch?v=5NDozsGMWIg
- Slides: https://hosted-files.sched.co/kccnceu2022/53/KubeCon2022_LT4_GRABNER_Thank%20you%20Keptn%20Obvious.pptx
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5NDozsGMWIg
- YouTube title: Lightning Talk: Thank you Keptn Obvious! Making SLOs observable with Prometheus a... Andreas Grabner
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/kubecon-observability/2022/lightning-talk-thank-you-keptn-obvious-making-slos-observable-with-pro/5NDozsGMWIg.txt
- Transcript chars: 5882
- Keywords: captain, observability, prometheus, actually, making, trying, decisions, desired, orchestration, obvious, actionable, native, connect, always, observable, kubecon, slides, obviously

### Resumo baseado na transcript

all right well thanks first of all for being so dedicated to kubecon it's 5 30 on a beautiful day and you're here and not at the bars so thank you so much i also want to say thank you to olek he was supposed to give this talk but unfortunately he had to travel and leave early so i'll do my best to give him justice but the great slides that you see are actually from him so if you ever see all the ghana chefs then give him

### Excerpt da transcript

all right well thanks first of all for being so dedicated to kubecon it's 5 30 on a beautiful day and you're here and not at the bars so thank you so much i also want to say thank you to olek he was supposed to give this talk but unfortunately he had to travel and leave early so i'll do my best to give him justice but the great slides that you see are actually from him so if you ever see all the ghana chefs then give him some kudos talk today thank you captain obvious making observability actionable with prometheus and captain obviously i try to make it obvious i really like captain um my name is andy gregner i work for dynatrace during the day but i'm also a captain maintainer and a contributor and i really like to show you what we are doing with captain if you think captain if you heard about captain you think captain is yet another cicd tool and it's a if this standpoint is told that hopefully i prove you wrong because i want to give you a little different perspective on captain captain has also changed over the last couple of years but if you want to get shirts or heads we also have a booth at the pavilion so check us out tomorrow but let me first get into my talk i talk about observability making observability actionable and when i talk up and think about observability i think about essays sovs are using observability data to keep systems reliable and resilient but you may say well one does not simply do a sre well i counter i think actually captain makes it pretty simple this is a post from tarash he is a performance engineer at facebook and when he saw that captain two years ago when we were still at the early stages you already saw we are trying to bring the srv core principles to the cloud native community letting observability that you pull out from prometheus or any other observability frame that she had using this to drive those actions that actually keep the system reliable um so first of all let me get started on what problem we really want to solve we all know that modern cloud native systems are no longer simple you have a lot of different tools and you need to connect them in one way or the other which means you have to build a lot of point-to-point integrations and trying to put in also your ability to make better decisions i'm pretty sure some of these tools are familiar the question is how can you make better informed decisions if you don't have visibility well fortunately we obviously talk a lot about observability in this conference i

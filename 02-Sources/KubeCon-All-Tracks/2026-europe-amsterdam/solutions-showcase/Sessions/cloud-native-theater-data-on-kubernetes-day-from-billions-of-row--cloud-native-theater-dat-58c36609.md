---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Victoriya Kalmanovich", "Sr. Engineering Leader and Shahar Azulay", "groundcover"]
sched_url: https://kccnceu2026.sched.com/event/2EFzy/cloud-native-theater-data-on-kubernetes-day-from-billions-of-rows-to-sub-second-queries-for-k8s-stacks-victoriya-kalmanovich-sr-engineering-leader-and-shahar-azulay-groundcover
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+Billions+of+Rows+to+Sub-Second+Queries+for+K8s+Stacks+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Data on Kubernetes Day: From Billions of Rows to Sub-Second Queries for K8s Stacks - Victoriya Kalmanovich, Sr. Engineering Leader and Shahar Azulay, groundcover

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Victoriya Kalmanovich, Sr. Engineering Leader and Shahar Azulay, groundcover
- Schedule: https://kccnceu2026.sched.com/event/2EFzy/cloud-native-theater-data-on-kubernetes-day-from-billions-of-rows-to-sub-second-queries-for-k8s-stacks-victoriya-kalmanovich-sr-engineering-leader-and-shahar-azulay-groundcover
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+Billions+of+Rows+to+Sub-Second+Queries+for+K8s+Stacks+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Data on Kubernetes Day: From Billions of Rows to Sub-Second Queries for K8s Stacks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzy/cloud-native-theater-data-on-kubernetes-day-from-billions-of-rows-to-sub-second-queries-for-k8s-stacks-victoriya-kalmanovich-sr-engineering-leader-and-shahar-azulay-groundcover
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+Billions+of+Rows+to+Sub-Second+Queries+for+K8s+Stacks+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=G9Bt-7OHVBk
- YouTube title: Cloud Native Theater | Data on Kubernetes Day: From Billion... Victoriya Kalmanovich & Shahar Azulay
- Match score: 0.74
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-data-on-kubernetes-day-from-billions-of-rows-to-s/G9Bt-7OHVBk.txt
- Transcript chars: 26171
- Keywords: observability, basically, infrastructure, everything, whatever, logs, microservices, control, managed, vendor, native, actually, stored, premises, eventually, traces, complicated, source

### Resumo baseado na transcript

Um, before we present ourselves, just uh presenting what we're going to talk about. We're going to cover Kubernetes monitoring at scale, which is kind of uh what a lot of you people are, you know, about right now in in this big Kubernetes conference, right? And debugging a production issue that used to take us minutes suddenly took us hours because the observability tooling just didn't catch up with the new architecture. the visibility the visibility problems they got so bad that at some point the solution was just to move things back to the monolith and not because the microservices themselves were wrong but because we just couldn't see into them and that was the moment This we is something we see with a lot of different companies and a lot of different teams from you know small scale to very big scale. Eventually Kubernetes gives you a lot of power to scale both your teams that can work now independently and build microservices and kind of you know scale up scale out as a team and as a company but also the ability to scale your infrastructure right uh in very different and very uh agile ways.

### Excerpt da transcript

Hey everybody, great to be here. Um, before we present ourselves, just uh presenting what we're going to talk about. We're going to cover Kubernetes monitoring at scale, which is kind of uh what a lot of you people are, you know, about right now in in this big Kubernetes conference, right? So, we're going to talk about technologies around it, how to do it, and a few interesting suggestions that we might have for you. Um, as we were presented, I'm Shahara Zilai. I'm the CEO and co-founder of Ground Cover. ground cover is an observability platform full stack uh dealing with a different type of solution that we're going to talk about today for high scale Kubernetes monitoring >> and my name is Vicki Kalmanovich I've been an engineering leader for the last decade I worked for various industries and I really love building teams and building different types of products and I guess our story today begins with a startup that I worked at a few years ago it was a very very small startup and we were acquired by Walmart So all of a sudden we had this whole new world of new requirements and a gigantic scale that we had to support and we got the mandate uh you take your monolith you split everything to microservices and you support that scale.

You do whatever you need to do to support that scale. The move to microservices and the ephemeral nature of Kubernetes infrastructure introduced so much complexity that our team just completely lost the ability to see what we were doing and what the system was uh uh what what was happening within our system. And we tried to create all the microservices at once. And there were so many dependencies between the microservices. And just essentially this really tiny app that we all knew so well by heart suddenly became massive. Troubleshooting became guesswork which is a horrible thing. And debugging a production issue that used to take us minutes suddenly took us hours because the observability tooling just didn't catch up with the new architecture. the visibility the visibility problems they got so bad that at some point the solution was just to move things back to the monolith and not because the microservices themselves were wrong but because we just couldn't see into them and that was the moment that we realized observability was not a nice to have infrastructure it's a prerequisite to operating microservices >> what uh Vicki kind of talked about right now is a personal example right a personal story.

This we is something we see

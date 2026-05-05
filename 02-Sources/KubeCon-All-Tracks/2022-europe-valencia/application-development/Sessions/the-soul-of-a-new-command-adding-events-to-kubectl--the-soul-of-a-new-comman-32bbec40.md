---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["Kubernetes Core"]
speakers: ["Bryan Boreham", "Grafana Labs"]
sched_url: https://kccnceu2022.sched.com/event/ytoe/the-soul-of-a-new-command-adding-events-to-kubectl-bryan-boreham-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=The+Soul+of+a+New+Command%3A+Adding+%E2%80%98Events%E2%80%99+to+kubectl+CNCF+KubeCon+2022
slides: []
status: parsed
---

# The Soul of a New Command: Adding ‘Events’ to kubectl - Bryan Boreham, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Bryan Boreham, Grafana Labs
- Schedule: https://kccnceu2022.sched.com/event/ytoe/the-soul-of-a-new-command-adding-events-to-kubectl-bryan-boreham-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=The+Soul+of+a+New+Command%3A+Adding+%E2%80%98Events%E2%80%99+to+kubectl+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre The Soul of a New Command: Adding ‘Events’ to kubectl.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytoe/the-soul-of-a-new-command-adding-events-to-kubectl-bryan-boreham-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=The+Soul+of+a+New+Command%3A+Adding+%E2%80%98Events%E2%80%99+to+kubectl+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YI1ZuN-OHNw
- YouTube title: The Soul of a New Command: Adding ‘Events’ to kubectl - Bryan Boreham, Grafana Labs
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/the-soul-of-a-new-command-adding-events-to-kubectl/YI1ZuN-OHNw.txt
- Transcript chars: 25369
- Keywords: events, command, server, object, little, cuddle, called, namespace, version, cattle, powerful, reason, objects, anyway, better, deployment, issues, anything

### Resumo baseado na transcript

this on ah that's better okay hi morning this uh i expected like six people um so thank you all for coming do we uh yeah okay so um i got a lot to get through uh the slides are on the the scad app uh so if if i skip over something you can download and look things up um okay who uh who who programs in go oh at least half okay that's pretty good there's going to be there's going to be some go code who likes

### Excerpt da transcript

this on ah that's better okay hi morning this uh i expected like six people um so thank you all for coming do we uh yeah okay so um i got a lot to get through uh the slides are on the the scad app uh so if if i skip over something you can download and look things up um okay who uh who who programs in go oh at least half okay that's pretty good there's going to be there's going to be some go code who likes yaml wow okay um so i uh i work at grafana labs for the first year and uh that's that's not particularly relevant to the talk but they do pay me more importantly you should follow me on twitter um so i am going to talk about adding a command to cube cuddle uh the command is called cube cuddle events or right now cube cattle alpha events um so we'll start with um how did i get here i i basically have no idea uh or i had no idea how to add a command to cubekiddle nor did i ever think i would um but i i was working on this thing uh k-span uh who who's seen that a couple of people so it's pretty cool i won't talk about it um but uh go go look it up it it it gives you a graphical view of events out of your kubernetes system um so let's just clarify what it what do i mean what am i talking about with events can i do lasers yeah not really i need a like a more powerful laser um so uh events are little little messages emitted by different parts of your kubernetes system maybe from your own code or maybe from part of the system like cubelet or the scheduler or really any part of the system and they they go into the api server and uh let's take a look this this is the sort of typical user experience of events uh you run kubectl get events and you get um you've got some events out you uh each one has a type which is either normal or warning h1 has a short form reason um it has an object here that it relates to and a sort of human readable message um so okay so far okay we've seen this right okay so i just want to adjust this slightly there we go um [Music] so this is what an event looks like if you were to print one out in yaml uh and it's kind of kind of the same stuff right we got the we got the message we got the reason uh we got a few more things like where did it come from um and the events are kubernetes objects uh so in the sense that they are the same thing to the api server as a pod or a deployment or pv or you know any any of the other uh objects within the kubernetes system so they have metadata they have a name they have a namespace a kind and a version

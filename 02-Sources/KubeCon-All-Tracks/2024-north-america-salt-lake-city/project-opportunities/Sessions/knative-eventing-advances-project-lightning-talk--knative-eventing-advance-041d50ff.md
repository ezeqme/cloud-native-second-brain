---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW9H/knative-eventing-advances-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Knative%3A+Eventing+Advances+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Knative: Eventing Advances | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW9H/knative-eventing-advances-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Knative%3A+Eventing+Advances+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Knative: Eventing Advances | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW9H/knative-eventing-advances-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Knative%3A+Eventing+Advances+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Rhe0UCDCbBA
- YouTube title: Knative: Eventing Advances | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/knative-eventing-advances-project-lightning-talk/Rhe0UCDCbBA.txt
- Transcript chars: 3915
- Keywords: events, eventing, broker, advanced, easily, security, received, resource, running, background, control, advances, recall, conative, architecture, securely, within, correct

### Resumo baseado na transcript

thank you everybody for coming uh my name is Leo I'm a current final year computer engineer student at University of Toronto and I was the one of the ctive venting maintainer So today we're going to talk about Eventing advance so first let's recall what is conative Eventing so conative Eventing is a platform that's allow you to quickly and uh easily build your event driven architecture uh on kubernetes and make your events flow easily and securely within your system um so on the left you can see be scaled down after a period of time if they didn't get any uh requ new traffic got received so it is designed to run like the stateless and short tasks it's not designed for running like a really long background jobs so can job and where should the destination to be so this advances uh components like including the security features new resource job sync uh and Advanced Event fering so uh it's actually represent a major step forward for K Eventing so together uh they address the three pillar of the modern Cloud native uh uh event architecture the security flexibilities and transparency uh yeah so that's the whole talk and thank you and stay you can scan the C to stay connected with the community and thank you [Applause]

### Excerpt da transcript

thank you everybody for coming uh my name is Leo I'm a current final year computer engineer student at University of Toronto and I was the one of the ctive venting maintainer So today we're going to talk about Eventing advance so first let's recall what is conative Eventing so conative Eventing is a platform that's allow you to quickly and uh easily build your event driven architecture uh on kubernetes and make your events flow easily and securely within your system um so on the left you can see that we have the events and we have our message broker in the at the at the center and on the right we have the sync which is our event receiver so events will arrive at the broker and the broker will take the responsibilities to transport the events to the correct destinations so this is really high level overview of ctive Eventing um and there are there many other components like triggers which connects the uh broker and the sync and the channels which will broadcast all is got uh received so if you want to learn more check out the kin.

the website to learn more so uh so today we're going to go over actually three Advanced uh Eventing topics the first three uh due to the time short shortage the first one is going to be security and the job sync and the Advanced Event fering so what is the security in K Eventing so in Eventing we have added the uh oidc support which means you can U add authentic ation and authorizations to the all the communications between the broker and your services so to visualize it uh impowered by this Eventing component you can configure who is allowed to send the event to who so why we're making efforts and why this matters uh we are aiming to make sure uh the events can flow within your system easily and securely so yeah uh next introducing the uh new resource called job sync so job sync is a resource that you can use to create a long running asynchronous job in your background so with the Autos scaling from the ctive serving ctive service service will be scaled down after a period of time if they didn't get any uh requ new traffic got received so it is designed to run like the stateless and short tasks it's not designed for running like a really long background jobs so can job think try to solve the problem it will create a long running and asynchronous job at the background uh with every unique event it's got received so here are some uh use use cases for example you wanted to uh trigger like a database backup jobs or uh when you got s

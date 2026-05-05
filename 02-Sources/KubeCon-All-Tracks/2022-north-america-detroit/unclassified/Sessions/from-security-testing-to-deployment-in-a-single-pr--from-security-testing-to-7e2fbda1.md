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
themes: ["Security", "GitOps Delivery"]
speakers: ["Sarah Khalife", "GitHub", "Grant Griffiths", "Portworx"]
sched_url: https://kccncna2022.sched.com/event/182FS/from-security-testing-to-deployment-in-a-single-pr-sarah-khalife-github-grant-griffiths-portworx
youtube_search_url: https://www.youtube.com/results?search_query=From+Security+Testing+To+Deployment+In+a+Single+PR+CNCF+KubeCon+2022
slides: []
status: parsed
---

# From Security Testing To Deployment In a Single PR - Sarah Khalife, GitHub & Grant Griffiths, Portworx

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Security]], [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Sarah Khalife, GitHub, Grant Griffiths, Portworx
- Schedule: https://kccncna2022.sched.com/event/182FS/from-security-testing-to-deployment-in-a-single-pr-sarah-khalife-github-grant-griffiths-portworx
- Busca YouTube: https://www.youtube.com/results?search_query=From+Security+Testing+To+Deployment+In+a+Single+PR+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre From Security Testing To Deployment In a Single PR.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182FS/from-security-testing-to-deployment-in-a-single-pr-sarah-khalife-github-grant-griffiths-portworx
- YouTube search: https://www.youtube.com/results?search_query=From+Security+Testing+To+Deployment+In+a+Single+PR+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rccqBUTW_SQ
- YouTube title: From Security Testing To Deployment In a Single PR - Sarah Khalife, GitHub & Grant Griffiths
- Match score: 0.81
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/from-security-testing-to-deployment-in-a-single-pr/rccqBUTW_SQ.txt
- Transcript chars: 36380
- Keywords: actually, security, request, scanning, vulnerabilities, developer, couple, database, source, vulnerability, swagger, working, application, understand, actions, requests, talking, github

### Resumo baseado na transcript

hey everybody thanks for coming Thanks For Walking in this room pretty far down the hallway so thanks for coming on Friday really appreciate that so today we'll be talking about from security testing to deployment in a single PR we'll be covering a lot of different things of how you can start a lot of your Automation and incorporating security earlier on just for quick introductions I'm Sarah Khalifa I'm a Solutions engineer at GitHub previously I was working on a lot of cloud native Cloud platform kind of

### Excerpt da transcript

hey everybody thanks for coming Thanks For Walking in this room pretty far down the hallway so thanks for coming on Friday really appreciate that so today we'll be talking about from security testing to deployment in a single PR we'll be covering a lot of different things of how you can start a lot of your Automation and incorporating security earlier on just for quick introductions I'm Sarah Khalifa I'm a Solutions engineer at GitHub previously I was working on a lot of cloud native Cloud platform kind of deployments worked on a lot of microservices but now over at the GitHub side um what else do I have here uh for fun I enjoy playing volleyball traveling and so happy to be here in Detroit and getting to check out Detroit um this time around and I'm Grant Griffis I'm a member and I've been at Fort Worth been at works for four years now uh previously I was at GE uh working on the platform team over there also also a contributor to Sig storage and kubernetes CSI so I'm involved in the kubernetes community and for fun I like to go climbing surfing and trail running in fact that's actually all right so today we'll be talking about well it's working either it's okay we can just use the one today we'll be talking about our agenda here so we'll be starting off with our introductions and overview of why we're even doing this what are some of our some of our motivations we'll be covering our security scanning our Automation and CI and then we'll actually jump into a live demo so it's not just slides it's more of a demo and we think that's more important kind of to show it live as we're working through it and then we'll take we'll finish it off with some of the takeaways and benefits of some of the processes that we're following all right first production and overview so actually previously in 2020 we did a session at kubecon kubecon Europe 2020 around automating with kubernetes and Docker so kind and building out your CI pipeline in a single PR so we talked about what is kind we talked about how you can actually trigger multiple versions of kubernetes using kind to run all of your testing because we know not one application is going to run on the same environment in every in every deployment that there is so this year we're kind of taking that to the next level we talked about Automation in the PR but now we're taking Automation and including security into it foreign so some of the some of the things we'll be covering today we'll be we'll be talking about some of

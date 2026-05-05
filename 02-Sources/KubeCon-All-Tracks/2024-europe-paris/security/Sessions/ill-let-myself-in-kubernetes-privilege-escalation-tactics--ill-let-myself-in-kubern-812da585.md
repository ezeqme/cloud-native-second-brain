---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["AI ML", "Security", "Kubernetes Core", "SRE Reliability"]
speakers: ["Andrew Martin", "Iain Smart", "ControlPlane"]
sched_url: https://kccnceu2024.sched.com/event/1YeR0/ill-let-myself-in-kubernetes-privilege-escalation-tactics-andrew-martin-iain-smart-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=I%27ll+Let+Myself+In%3A+Kubernetes+Privilege+Escalation+Tactics+CNCF+KubeCon+2024
slides: []
status: parsed
---

# I'll Let Myself In: Kubernetes Privilege Escalation Tactics - Andrew Martin & Iain Smart, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Andrew Martin, Iain Smart, ControlPlane
- Schedule: https://kccnceu2024.sched.com/event/1YeR0/ill-let-myself-in-kubernetes-privilege-escalation-tactics-andrew-martin-iain-smart-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=I%27ll+Let+Myself+In%3A+Kubernetes+Privilege+Escalation+Tactics+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre I'll Let Myself In: Kubernetes Privilege Escalation Tactics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeR0/ill-let-myself-in-kubernetes-privilege-escalation-tactics-andrew-martin-iain-smart-controlplane
- YouTube search: https://www.youtube.com/results?search_query=I%27ll+Let+Myself+In%3A+Kubernetes+Privilege+Escalation+Tactics+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=f10WQlr0h_M
- YouTube title: I'll Let Myself In: Kubernetes Privilege Escalation Tactics - Andrew Martin & Iain Smart
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/ill-let-myself-in-kubernetes-privilege-escalation-tactics/f10WQlr0h_M.txt
- Transcript chars: 28472
- Keywords: cluster, security, actually, probably, basically, attacker, access, namespace, hopefully, trying, create, running, someone, quickly, binding, developer, permissions, secrets

### Resumo baseado na transcript

I will get started 5 minutes early because knowing me I'm probably going to go slightly over hopefully you are all here for an adventure in container security breaking into kubernetes clusters uh this is I'll let myself in very quick introduction um the astute among you may notice that there's only one of me up here unfortunately Andy has not been able to join us today so you're stuck with me for the next 35 minutes uh I'm Ian I'm an uh security consultant at control plane uh I system design and it should be always what's the worst thing that could possibly happen think about that before you start building anything so the first thing we would generally do um if you've decided right we've got something ready we've got it built we'd like it looked at is a a pen test and basically sorry this bottle doesn't fit on the Shelf basically um let's try and break in this is basically security QA so instead of doing QA and checking that your app doesn't break when you star in my own namespace so I'm just going to demonstrate that with another CU C off can I and effectively somewhere up here so you can see at the top there I've got star. star in my own namespace this is an escalation that I found recently that I was genuinely surprised by this is working as intended by Design if you have star.

### Excerpt da transcript

I will get started 5 minutes early because knowing me I'm probably going to go slightly over hopefully you are all here for an adventure in container security breaking into kubernetes clusters uh this is I'll let myself in very quick introduction um the astute among you may notice that there's only one of me up here unfortunately Andy has not been able to join us today so you're stuck with me for the next 35 minutes uh I'm Ian I'm an uh security consultant at control plane uh I am on the offensive security team which means I get to say I'm offensive and not actually offend people I hope um and I have spent the last few years working in penetration testing and breaking into various things but over the Last 5 Years kubernetes clusters CI platforms all things kind of Dev psych opsy so hopefully you're all here to hear something like this we're going to talk a little bit briefly about what offse SEC is hopefully a bunch of people are familiar with this already if you're not we'll just Define kind of why do we do offensive security why do you need it we'll talk about some common findings we'll do some demos we hopefully won't need to resort to the recorded demos don't know we'll find out um we'll talk a bit about post compromise activities which is an area that I've seen a lot of people not particularly pay much attention to and then we'll do another demo hopefully although I think my final demo might actually be broken but we shall see so at a very high level the problem that offensive security teams are trying to solve is that kubernetes is complicated I hope this isn't a shock to anyone hopefully everyone knows that it's not the easiest thing in the world to manage and I don't just mean it's complicated I mean if you're an organization who's running kubernetes or any of these kind of orchestration systems there are so many moving Parts out there and I I genuinely don't think most people know what all the parts do how they work how they talk to each other I think we see a lot of people deploying really complicated solutions to basically host a single web app or to to host something that they don't really understand they're just going right this is the cool shiny thing it's on Hacker News let's use it I think that leads to a lots of people running stuff that they just do not know what's happening there's also the rate of change I think we're all probably familiar with the Relentless release cycle of kubernetes and how you need to keep up to date because otherw

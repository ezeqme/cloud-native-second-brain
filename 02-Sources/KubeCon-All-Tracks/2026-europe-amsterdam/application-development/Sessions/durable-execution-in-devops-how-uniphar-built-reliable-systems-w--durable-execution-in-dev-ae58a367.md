---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Alice Gibbons", "Diagrid", "Vaclav (Oisin) Haken", "Uniphar"]
sched_url: https://kccnceu2026.sched.com/event/2CW2R/durable-execution-in-devops-how-uniphar-built-reliable-systems-with-dapr-alice-gibbons-diagrid-vaclav-oisin-haken-uniphar
youtube_search_url: https://www.youtube.com/results?search_query=Durable+Execution+in+DevOps%3A+How+Uniphar+Built+Reliable+Systems+with+Dapr+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Durable Execution in DevOps: How Uniphar Built Reliable Systems with Dapr - Alice Gibbons, Diagrid & Vaclav (Oisin) Haken, Uniphar

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alice Gibbons, Diagrid, Vaclav (Oisin) Haken, Uniphar
- Schedule: https://kccnceu2026.sched.com/event/2CW2R/durable-execution-in-devops-how-uniphar-built-reliable-systems-with-dapr-alice-gibbons-diagrid-vaclav-oisin-haken-uniphar
- Busca YouTube: https://www.youtube.com/results?search_query=Durable+Execution+in+DevOps%3A+How+Uniphar+Built+Reliable+Systems+with+Dapr+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Durable Execution in DevOps: How Uniphar Built Reliable Systems with Dapr.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW2R/durable-execution-in-devops-how-uniphar-built-reliable-systems-with-dapr-alice-gibbons-diagrid-vaclav-oisin-haken-uniphar
- YouTube search: https://www.youtube.com/results?search_query=Durable+Execution+in+DevOps%3A+How+Uniphar+Built+Reliable+Systems+with+Dapr+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=REp5yMgy7UQ
- YouTube title: Durable Execution in DevOps: How Uniphar Built Reliable Syst... Alice Gibbons & Vaclav (Oisin) Haken
- Match score: 0.873
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/durable-execution-in-devops-how-uniphar-built-reliable-systems-with-da/REp5yMgy7UQ.txt
- Transcript chars: 28214
- Keywords: workflow, workflows, dapper, application, little, business, resources, wanted, number, within, running, cost, actually, ultimately, resource, essentially, eventually, execution

### Resumo baseado na transcript

Specifically, I have my friend from UniFar here and we are going to talk about how they built distributed systems that were reliable with Dapper and I and I have a clicker and I'm going to use my clicker. I'm head of the customer engineering team at DiGrid, which is the company behind the open source Dapper project. We are as I said part of the CNCF as well as the AIF and yeah we want to talk a lot about reliability today. So this particular example solution is is is a lot to do with uh with cost management and that's how we refer to it and ultimately you know when I described Unifor I mentioned that it kind of grew over all those decades and a And so the cost management is really an important aspect because it would be very easy to just migrate some beefy servers from on-prem to cloud and you know eventually though you get the bill right because clouds can be very expensive. So we wanted to allow for some kind of splitting of a cost between these initiatives.

### Excerpt da transcript

Um, thank you so much for coming. Today we are going to talk to you about durable execution in DevOps. Specifically, I have my friend from UniFar here and we are going to talk about how they built distributed systems that were reliable with Dapper and I and I have a clicker and I'm going to use my clicker. Oh, I did it twice. Okay, thanks so much for coming. My name is Alice Gibbons. I'm head of the customer engineering team at DiGrid, which is the company behind the open source Dapper project. Um, and yeah, we're going to talk a lot about reliability in distributed systems today, specifically around workflow. And with me, I have my friend Osheen. >> Hello, my name is Oshin and I work for UniFor and I'm a member of a I'm a cloud developer. I work for kind of DevOps and platform engineering. So yeah, we're going to show you how we use Dapper, >> right? So I probably should start a little bit with you know just telling you what UniFar actually is. So, Unifir was really uh like a small little kind of co-op of fewarmacies back in 1967 and it kind of grew a little bit you know so now it's going to be an big anniversary coming soon next year and it's it's now in 160 plus countries and 200 plus multinational partners.

And the whole idea is really just to, you know, give people critical life-saving drugs when they need to and just as well do it in just the easiest way possible, which ultimately, you know, translates to cost and uh so really cover the whole end to end, give you a lot of expertise that we've accumulated so far, tailor solutions to your needs, and ultimately do it now in a in a modern way because uh originally it would have been you know, Tony calling John and ordering stuff over the phone and now it's all going to be or is already digital. >> Awesome. And yeah, we if you haven't heard of Diagram before, as I said, we're the company behind the open source Dapper project, which is now a graduated project in the CNCF. And essentially our our primary goal is to build platform and services for distributed and reliable applications, including you know AI agents, workflows, um everything you know that from there. We are as I said part of the CNCF as well as the AIF and yeah we want to talk a lot about reliability today.

>> Okay. So this particular example solution is is is a lot to do with uh with cost management and that's how we refer to it and ultimately you know when I described Unifor I mentioned that it kind of grew over all those decades and a lot

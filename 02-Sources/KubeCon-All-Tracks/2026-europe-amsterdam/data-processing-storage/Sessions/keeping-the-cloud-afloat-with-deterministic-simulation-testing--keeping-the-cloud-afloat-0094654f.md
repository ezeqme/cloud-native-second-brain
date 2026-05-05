---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["Storage Data"]
speakers: ["Marcus Hodgson", "Antithesis", "Marek Siarkowicz", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CW6k/keeping-the-cloud-afloat-with-deterministic-simulation-testing-marcus-hodgson-antithesis-marek-siarkowicz-google
youtube_search_url: https://www.youtube.com/results?search_query=Keeping+the+Cloud+Afloat+with+Deterministic+Simulation+Testing+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Keeping the Cloud Afloat with Deterministic Simulation Testing - Marcus Hodgson, Antithesis & Marek Siarkowicz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marcus Hodgson, Antithesis, Marek Siarkowicz, Google
- Schedule: https://kccnceu2026.sched.com/event/2CW6k/keeping-the-cloud-afloat-with-deterministic-simulation-testing-marcus-hodgson-antithesis-marek-siarkowicz-google
- Busca YouTube: https://www.youtube.com/results?search_query=Keeping+the+Cloud+Afloat+with+Deterministic+Simulation+Testing+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Keeping the Cloud Afloat with Deterministic Simulation Testing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6k/keeping-the-cloud-afloat-with-deterministic-simulation-testing-marcus-hodgson-antithesis-marek-siarkowicz-google
- YouTube search: https://www.youtube.com/results?search_query=Keeping+the+Cloud+Afloat+with+Deterministic+Simulation+Testing+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qgCpdb2sbh8
- YouTube title: Keeping the Cloud Afloat with Deterministic Simulation Testing - Marcus Hodgson & Marek Siarkowicz
- Match score: 0.875
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/keeping-the-cloud-afloat-with-deterministic-simulation-testing/qgCpdb2sbh8.txt
- Transcript chars: 24436
- Keywords: antithesis, leader, testing, correctness, explore, heartbeat, second, previous, timeline, happens, knowledge, basically, timelines, follower, deterministic, validation, failure, faults

### Resumo baseado na transcript

I I'm a TL of SIG at CD and I work in Kubernetes scalability and API machinery performance. So today we're going to talk about deterministic simulation testing um, and how CD made use of antithesis to explore and test its massive state space. So it's our number one priority but with 12 year old uh code base uh maintainer rotation and very hard to verify guarantees this became a real challenge to community to maintain um our guarantees uh for long period or over time. mean required multi-layered knowledge to from multiple parts of codebase to find um so to address that and take learnings the community built a robustness testing framework that was inspired by Jeepson and we used uh model based validation uh from mo like model testing uh to to validate the correctness. But that unfortunately showed us that solving the problem is just the first step. So uh first the verifying correctness is uh using model is an NP hard problem of tracing the history of all the events and this makes it really fragile and high maintenance.

### Excerpt da transcript

Yep. My name is Marcus. Uh, I work at Antithesis and we do software testing. >> And I'm Mark. I work at Google. I I'm a TL of SIG at CD and I work in Kubernetes scalability and API machinery performance. Cool. So today we're going to talk about deterministic simulation testing um, and how CD made use of antithesis to explore and test its massive state space. So what are we going to cover? Um there going to be four main sections to this talk and we're going to go through them each one by one uh and try to get through them all in just 20 minutes. So for the first uh we're going to go over Etsy's history of correctness where Mark is going to talk about some of the uh challenges that he and the maintainers had faced and what they had done to solve them. Uh then we're going to talk about antithesis. So what is it? How does it work? Uh why is testing with antithesis a super powerful way of testing? Uh third, we're going to go over the integration between the two. So how we put CD under test into antithesis. And lastly, we'll be going over a case study of a really recent and tricky correctness bug.

So we'll talk about how we found it, uh how we debugged it, and how we solved it. Yeah, a little bit context on the correctness. uh so HD is the source of truth for Kubernetes and any critical infrastructure information. So uh for us the reliability and correctness of it is the critical foundation of everything and that happens on this conference and all the projects around it. So it's our number one priority but with 12 year old uh code base uh maintainer rotation and very hard to verify guarantees this became a real challenge to community to maintain um our guarantees uh for long period or over time. So uh during a 3.5 release around 3 four years ago we uh the maintainer rotation uh led to a lot of knowledge un uh not being written led to it a lot of testing being missed which uh which allowed uh some bugs to slip in. So the the new maintainers that came in didn't have enough experience, couldn't validate and there was a lot of pressure to to to move on and um and develop uh the system forward.

But unfortunately the reviewers were not experienced enough to catch each segment and and all the bugs were very tricky. mean required multi-layered knowledge to from multiple parts of codebase to find um so to address that and take learnings the community built a robustness testing framework that was inspired by Jeepson and we used uh model based validation uh from mo like

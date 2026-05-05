---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Nabarun Pal", "Broadcom"]
sched_url: https://kccnceu2026.sched.com/event/2CW0S/policy-engines-for-kubernetes-picking-one-without-losing-your-mind-nabarun-pal-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Policy+Engines+for+Kubernetes%3A+Picking+One+Without+Losing+Your+Mind+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Policy Engines for Kubernetes: Picking One Without Losing Your Mind - Nabarun Pal, Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nabarun Pal, Broadcom
- Schedule: https://kccnceu2026.sched.com/event/2CW0S/policy-engines-for-kubernetes-picking-one-without-losing-your-mind-nabarun-pal-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Policy+Engines+for+Kubernetes%3A+Picking+One+Without+Losing+Your+Mind+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Policy Engines for Kubernetes: Picking One Without Losing Your Mind.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0S/policy-engines-for-kubernetes-picking-one-without-losing-your-mind-nabarun-pal-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Policy+Engines+for+Kubernetes%3A+Picking+One+Without+Losing+Your+Mind+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y5rrfSZBm1A
- YouTube title: Policy Engines for Kubernetes: Picking One Without Losing Your Mind - Nabarun Pal, Broadcom
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/policy-engines-for-kubernetes-picking-one-without-losing-your-mind/y5rrfSZBm1A.txt
- Transcript chars: 32220
- Keywords: policy, actually, policies, resources, native, resource, infrastructure, gatekeeper, language, running, engine, simple, enforcement, cluster, requirements, admission, production, cost

### Resumo baseado na transcript

Uh thank you for making it to one of the last talks on the first day of the conference. Today I'm going to talk about something that sounds simple but gets complicated really fast. This result in like real money savings, real cost control and again these are all numbers made up just to prove a point. Um the answer may be drastically different uh different depending on do they need to learn like 2 days of AML or do they need two to four weeks of training on some other policy engine language and it can make a day and night So when we talk about web hooks in the Kubernetes space, there's always a question on what is the failure mode. Although there are some gotchas that we will come into uh you have to keep those in mind while you try to uh vet Kubernetes native validating admission policies.

### Excerpt da transcript

Welcome everyone. Uh thank you for making it to one of the last talks on the first day of the conference. I am happy seeing like so many people around. Um I am Nabarun. Today I'm going to talk about something that sounds simple but gets complicated really fast. Policy enforcement in Kubernetes. So can you all raise your hand? Oh, even before I ask the question, we have some hands. Um, did you ever have a pod running as root in production that should not have been that way? Huh? And how many of you keep your hands up and how many of you figured it out during an incident and not actually because of a policy violation? Oh, not many. So, you all know about policy. Why are you in this talk then? Okay, let's still go ahead. Uh, oh, seems like I have been going through slides. Um, so we're going to look at a framework and a few of the solutions that are available in the cloud native ecosystem to do policy inform enforcement in Kubernetes. And I hope by the end of the session you have some idea about like what solution to choose in what scenario and how you can migrate between the solutions like when you grow or when you scale down um your infrastructure.

Um policy enforcement does sound very simple but it is not. It only sounds simple on paper. Um I'm sure like some of these points might close head to home. uh 42 teams um analogy is my favorite. Um we feel like things might have been solved but often what happens is different teams have a different way to handle policy and they might result in like different things or you might have different products running on the same infrastructure which might have their own opinions on doing policy enforcement. Uh it also looks very trivial until you try to do it at scale. Let's say if you have like 10,000 policies um which I hope you don't have in a single cluster but there are instances where you are running multi-enant apps and you can run into those kind of pitfalls. So let's talk some real world scenarios on like why you are here. Compliance requirements let's face it so HIPPA uh PCI GDPR we all uh might have gone into things um in those directions. Now, whenever you have an audit going, there's a difference between we have an policy as an answer and you telling and showing your auditor the exact audit log on what was audited, when it was audited and the decisions that led to the audit that gives the actual value.

The second answer actually passes the audits and that is what auditors need the audit trail or the audit

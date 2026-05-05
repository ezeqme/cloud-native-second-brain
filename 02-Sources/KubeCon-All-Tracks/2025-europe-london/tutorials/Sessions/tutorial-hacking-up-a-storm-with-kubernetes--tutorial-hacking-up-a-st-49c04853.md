---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Tutorials"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Rory McCune", "Datadog", "Marion McCune", "ScotSTS", "Iain Smart", "AmberWolf"]
sched_url: https://kccnceu2025.sched.com/event/1tx72/tutorial-hacking-up-a-storm-with-kubernetes-rory-mccune-datadog-marion-mccune-scotsts-iain-smart-amberwolf
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Hacking+up+a+Storm+With+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Tutorial: Hacking up a Storm With Kubernetes - Rory McCune, Datadog; Marion McCune, ScotSTS; Iain Smart, AmberWolf

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Tutorials]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Rory McCune, Datadog, Marion McCune, ScotSTS, Iain Smart, AmberWolf
- Schedule: https://kccnceu2025.sched.com/event/1tx72/tutorial-hacking-up-a-storm-with-kubernetes-rory-mccune-datadog-marion-mccune-scotsts-iain-smart-amberwolf
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Hacking+up+a+Storm+With+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Tutorial: Hacking up a Storm With Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx72/tutorial-hacking-up-a-storm-with-kubernetes-rory-mccune-datadog-marion-mccune-scotsts-iain-smart-amberwolf
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Hacking+up+a+Storm+With+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8Q8sFzODEUo
- YouTube title: Tutorial: Hacking up a Storm With Kubernetes - Rory McCune, Datadog; Marion McCune & Iain Smart
- Match score: 0.736
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/tutorial-hacking-up-a-storm-with-kubernetes/8Q8sFzODEUo.txt
- Transcript chars: 53649
- Keywords: cluster, create, namespace, security, rights, actually, arbback, account, permissions, running, useful, admission, escalate, working, anyone, control, clusters, always

### Resumo baseado na transcript

Uh very glad to see you all decided to come to the tutorial and not go outside in the sun and get an ice cream and a cold drink. Um what we want to do this afternoon is we want to teach a bit about Kubernetes security through a hacking scenario. So, we're going to take one attack and we're going to walk through several steps of bypassing and avoiding Kubernetes security controls to show us how someone might be able to escalate their privileges in a way that perhaps we didn't expect they would be able to do. What we're going to do is throughout the tutorial, we are going to play the part of a developer who is writing some software which is going to run in a Kubernetes cluster. And unfortunately, they're going to encounter some problems and we'll need to get creative. And it's that act of getting creative in which we're going to find some hopefully interesting Kubernetes security facts that we're going to work around.

### Excerpt da transcript

Afternoon everyone and uh welcome along to this afternoon's tutorial. Uh very glad to see you all decided to come to the tutorial and not go outside in the sun and get an ice cream and a cold drink. Um what we want to do this afternoon is we want to teach a bit about Kubernetes security through a hacking scenario. My goal for the tutorial today is I hope that everyone in the room leaves with at least one new thing they didn't know about Kubernetes security. That's my personal goal. So if we can get to that point, it will have been a success for me anyway. Um about us, you might have noticed on the schedule there were three of us. Unfortunately, life sometimes happens and not everyone can make it. Uh so I am Rory uh and I will be running the tutorial today. Uh I've been doing container security now for around uh nine years. Uh and I do a number of things like help out with Kubernetes SIG security and also help maintain the CIS benchmarks for Docker and Kubernetes. So if you've ever had a bad CI CIS compliance finding and you're wondering who to blame, I'm the guy.

Um also uh if you're this tutorial sparks an interest in Kubernetes security in you, then SIG security is a great place to learn more. We have meetings every other week. Uh I think the booth will probably be shutting fairly soon, but we are around on Slack as well. Uh and my partners in crime who unfortunately can't make it are Ian and Marian. So let's start. What are we going to do? We are going to follow an attack path in Kubernetes. So, we're going to take one attack and we're going to walk through several steps of bypassing and avoiding Kubernetes security controls to show us how someone might be able to escalate their privileges in a way that perhaps we didn't expect they would be able to do. Um, and we're going to explain the concepts at each step. So, we want to walk through and actually explain what we're doing and why this works and also to an extent why it might be surprising to people that this is how it all works and hangs together. logistics. Um, phones on silent if anyone has phone ringers on these days.

I don't know if you do, but best not to. Uh, you can work in practice. So, we're definitely going to have the idea is everyone who wants to can follow along on local machines. If you don't want to do that or you at any point kind of get lost with it, do not worry. We will be going through every single step up on screen. So, you'll be able to get everything of what's going on just b

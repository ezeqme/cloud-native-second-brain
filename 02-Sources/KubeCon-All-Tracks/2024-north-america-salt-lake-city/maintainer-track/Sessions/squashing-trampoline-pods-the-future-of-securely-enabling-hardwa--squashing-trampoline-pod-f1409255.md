---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Joe Betz", "Google", "David Eads", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1howB/squashing-trampoline-pods-the-future-of-securely-enabling-hardware-extensions-joe-betz-google-david-eads-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Squashing+Trampoline+Pods%3A+The+Future+of+Securely+Enabling+Hardware+Extensions+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Squashing Trampoline Pods: The Future of Securely Enabling Hardware Extensions - Joe Betz, Google & David Eads, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Joe Betz, Google, David Eads, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1howB/squashing-trampoline-pods-the-future-of-securely-enabling-hardware-extensions-joe-betz-google-david-eads-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Squashing+Trampoline+Pods%3A+The+Future+of+Securely+Enabling+Hardware+Extensions+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Squashing Trampoline Pods: The Future of Securely Enabling Hardware Extensions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howB/squashing-trampoline-pods-the-future-of-securely-enabling-hardware-extensions-joe-betz-google-david-eads-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Squashing+Trampoline+Pods%3A+The+Future+of+Securely+Enabling+Hardware+Extensions+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qRo1Qw_Hr2A
- YouTube title: Squashing Trampoline Pods: The Future of Securely Enabling Hardware Extensions- Joe Betz, David Eads
- Match score: 0.965
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/squashing-trampoline-pods-the-future-of-securely-enabling-hardware-ext/qRo1Qw_Hr2A.txt
- Transcript chars: 19483
- Keywords: actually, access, authorization, resource, trampoline, request, admission, container, cluster, account, particular, restrict, selectors, attacker, write, requests, called, everything

### Resumo baseado na transcript

thanks everybody for joining today um I know it's at the end of a long day so I appreciate everybody taking the time to make it out for this one I'm Joe Betts um I'm joined by David eids we are both TL's of sigap machinery and today we're going to be talking about squashing pod trampolines before I go a bit further let's explain what that means um so a pod trampoline attack starts with a container breakout followed by a compromise of the node that container is on

### Excerpt da transcript

thanks everybody for joining today um I know it's at the end of a long day so I appreciate everybody taking the time to make it out for this one I'm Joe Betts um I'm joined by David eids we are both TL's of sigap machinery and today we're going to be talking about squashing pod trampolines before I go a bit further let's explain what that means um so a pod trampoline attack starts with a container breakout followed by a compromise of the node that container is on followed by an expansion of that attack out into the rest of the cluster either by jumping to additional nodes or by escalating privileges sounds fun right so I figured I'd let my kids try it um so what I did is I took a video game my kids been playing called pren simulator and created the level so the level has a container um a trampoline and then a and then a foam pit which represents access to the rest of your cluster so I'm going to go ahead and just let the kids start playing that and while they do let's explain a little bit about what's going on with the technology so a container breakout can be tricky but there can be misconfigurations in container infrastructure there can be vulnerabilities in that infrastructure or even in the kernel that can lead to opportunities to escape when that happens um the um attacker then has access to the rest of the node for the purpose of this talk we're just going to assume that the container breakouts can happen and our goal is to focus on minimizing the damage that happens when a container breakout does happen when um an attacker gets out of a container they're going to start using the resources available on the Node to try and expand their attack out to the rest of your cluster so they're going to have access to the volumes on that node they're going to have access to the service accounts and secrets and things like that and they're going to be looking for ways to leverage that as a way to trampoline off just that node which is you know only a small fraction of your infrastructure out to the rest of your infrastructure once they do that they now have access to everything that they could hope for right like they can get to all the information on all your nodes if they can if you have any service account anywhere with escalated privileges they're going to be able to get to that and the thing they're going to be looking for the most is the things with the broadest permissions and one of those things is a Damon set typically when you have platform extensions

---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Ian Coldwater", "Independent", "Tabitha Sable", "Rory McCune", "Datadog", "Iain Smart", "AmberWolf", "Mahé Tardy", "Isovalent at Cisco"]
sched_url: https://kccnceu2026.sched.com/event/2EF5n/a-bugs-eye-view-kubernetes-sig-security-explains-it-all-ian-coldwater-independent-tabitha-sable-rory-mccune-datadog-iain-smart-amberwolf-mahe-tardy-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=A+Bug%E2%80%99s-Eye+View%3A+Kubernetes+SIG+Security+Explains+It+All+CNCF+KubeCon+2026
slides: []
status: parsed
---

# A Bug’s-Eye View: Kubernetes SIG Security Explains It All - Ian Coldwater, Independent; Tabitha Sable & Rory McCune, Datadog; Iain Smart, AmberWolf; Mahé Tardy, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ian Coldwater, Independent, Tabitha Sable, Rory McCune, Datadog, Iain Smart, AmberWolf, Mahé Tardy, Isovalent at Cisco
- Schedule: https://kccnceu2026.sched.com/event/2EF5n/a-bugs-eye-view-kubernetes-sig-security-explains-it-all-ian-coldwater-independent-tabitha-sable-rory-mccune-datadog-iain-smart-amberwolf-mahe-tardy-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=A+Bug%E2%80%99s-Eye+View%3A+Kubernetes+SIG+Security+Explains+It+All+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre A Bug’s-Eye View: Kubernetes SIG Security Explains It All.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5n/a-bugs-eye-view-kubernetes-sig-security-explains-it-all-ian-coldwater-independent-tabitha-sable-rory-mccune-datadog-iain-smart-amberwolf-mahe-tardy-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=A+Bug%E2%80%99s-Eye+View%3A+Kubernetes+SIG+Security+Explains+It+All+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ujnqeWQZ17w
- YouTube title: A Bug’s-Eye View: Kubernetes SIG Security Explains It... Ian C, Tabitha S, Rory M, Iain S &  Mahé T
- Match score: 0.826
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/a-bugs-eye-view-kubernetes-sig-security-explains-it-all/ujnqeWQZ17w.txt
- Transcript chars: 29862
- Keywords: security, vulnerability, basically, wanted, software, information, actually, findings, anybody, vulnerabilities, official, important, tooling, response, committee, projects, working, writing

### Resumo baseado na transcript

Um, I am one of the co-chairs of Kubernetes SIG Security and you can find out more about my current full-time job at standwithmininnesota.com. Um, you are here at Kubernetes 6urities maintainer track talk, a bug's view. Kubernetes SIG security is a horizontal SIG that works in collaboration with other SIGs across the Kubernetes project to make the Kubernetes project more secure. Our overall title is that we work across SIGs to improve security content of Kubernetes documentation as well as independently create security docs in the form of concepts and blogs. And it's one of those projects as one that we spent a lot of time on this year that I really wanted to talk about because it's it's kind of an interesting one and it's outside of the main Kubernetes doc site. And OASP is an open source foundation that has a lot of things like software and documentation that generally attempt to improve software security.

### Excerpt da transcript

Hello, my name is Ian Coldwater, pronouns they them. Um, I am one of the co-chairs of Kubernetes SIG Security and you can find out more about my current full-time job at standwithmininnesota.com. Um, you are here at Kubernetes 6urities maintainer track talk, a bug's view. If you are here for a different talk, you're in the wrong room and that's cool. We're happy to see you. Anyway, this talk will be a little bit different from our previous maintainer track talks. Usually, we just give updates about what we're up to, and we do have some really cool updates for you today. But we also wanted to take this time this time around to go through not only what we've been doing, but how we do it. We wanted to talk about the process. We wanted to talk about how we think through these things and just kind of like the actual gears and how these things work for anybody who was curious or anybody who wasn't. So, um, we're going to go into what gets done and how we do it with a special guest appearance from the security response committee, who is not technically SIG security, but they're here today anyway.

Kubernetes SIG security is a horizontal SIG that works in collaboration with other SIGs across the Kubernetes project to make the Kubernetes project more secure. A lot of our work is done in our sub projects which we will be hearing from today. Um, our first update is from SIG Security Docs. Rory, tell us the latest. >> Awesome. Thank you. Uh, yeah. So, where are we slidewise? One more. Great. So, I Yeah, I'm here to talk to you about SIG security docs. Uh, if you want want to join us, uh, especially after hearing about what we get up to, we meet on the first Thursday of every month at 2 PM Eastern. I'm one of the co-chairs. My name is Rory McHune and our other co-chair is just there, Sabatha. Um, and we do a variety of things to try and help out with documentation. Our overall title is that we work across SIGs to improve security content of Kubernetes documentation as well as independently create security docs in the form of concepts and blogs. And it's one of those projects as one that we spent a lot of time on this year that I really wanted to talk about because it's it's kind of an interesting one and it's outside of the main Kubernetes doc site.

What we've been working on is the OASP Kubernetes top 10. So um a little background on OASP. OASP is the open worldwide application security project. If anyone knows OASP of old, you'll think, hang on, that's not what it s

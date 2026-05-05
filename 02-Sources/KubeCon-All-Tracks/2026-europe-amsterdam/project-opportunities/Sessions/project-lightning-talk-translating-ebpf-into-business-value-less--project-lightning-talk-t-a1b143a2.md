---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Bill Mulligan", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFwm/project-lightning-talk-translating-ebpf-into-business-value-lessons-from-the-cilium-website-bill-mulligan-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Translating+Ebpf+Into+Business+Value%3A+Lessons+From+The+Cilium+Website+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Translating Ebpf Into Business Value: Lessons From The Cilium Website - Bill Mulligan, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Bill Mulligan, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFwm/project-lightning-talk-translating-ebpf-into-business-value-lessons-from-the-cilium-website-bill-mulligan-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Translating+Ebpf+Into+Business+Value%3A+Lessons+From+The+Cilium+Website+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Translating Ebpf Into Business Value: Lessons From The Cilium Website.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFwm/project-lightning-talk-translating-ebpf-into-business-value-lessons-from-the-cilium-website-bill-mulligan-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Translating+Ebpf+Into+Business+Value%3A+Lessons+From+The+Cilium+Website+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=J4jHq2ExjJo
- YouTube title: Project Lightning Talk: Translating Ebpf Into Business Value: Lessons From The Cili... Bill Mulligan
- Match score: 0.972
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-translating-ebpf-into-business-value-lessons-fr/J4jHq2ExjJo.txt
- Transcript chars: 5180
- Keywords: trying, business, psyllium, network, actually, industry, actual, bottom, challenges, networking, outcome, software, source, policy, bloomberg, financial, features, selium

### Resumo baseado na transcript

And when we were at CubeCon Amsterdam 3 years ago, we were talking about EVPF, Psyllium, it's going to be the greatest thing. But a lot of the times when we're talking to people, they say, "Yeah, this bite code in the kernel, why does it even matter to my business?" And so I think a lot of things that we do in software, there's a disconnect between the code that we're writing and the capital that's actually driving the business. So whether that's something like multicluster networking or network policy or network observability and they're trying to solve those use cases because their industry has different types of challenges and to solve those industry challenges is what their business is trying to do and that's um they actually talked at Psyllium Con here 3 years ago and obviously financial services company what they're trying to do is care about um security and compliance. The feature uh that they're trying to use is network policy to secure their Kubernetes clusters. Well, in the financial services industry, obviously, you care about security, compliance, regulation.

### Excerpt da transcript

This is CubeCon number 20 for me, which makes me feel really old. I guess we're over a decade into cloud native now. And when we were at CubeCon Amsterdam 3 years ago, we were talking about EVPF, Psyllium, it's going to be the greatest thing. But a lot of the times when we're talking to people, they say, "Yeah, this bite code in the kernel, why does it even matter to my business?" And so I think a lot of things that we do in software, there's a disconnect between the code that we're writing and the capital that's actually driving the business. So that's what I'm going to try to talk to you about today. How can we connect the code that we're writing to the actual capital, the business, the bottom line that we're trying to affect. And when you're thinking about an open source project, you need to think about like what are the hierarchy of needs? like why is an actual user trying to come to your project and solve their challenges and in the past three years uh working on the psyllium project I've kind of come up with a framework of translating from the ebpf bite code that we have into insilium to the actual business bottom line and the way that I do that it all starts with the user right that's what we're trying to do with software we're trying to solve user problems we want people to use our software That's the cool thing about open source.

You know, EbF, it's used by every single Android phone in the world. The software that I write is deployed on billions of devices worldwide. That's pretty cool. That's why I love open source. So going up from there, connecting it back to the business, what the users are actually trying to solve is a specific use case that they may have in the business. So whether that's something like multicluster networking or network policy or network observability and they're trying to solve those use cases because their industry has different types of challenges and to solve those industry challenges is what their business is trying to do and that's the outcome that they're trying to have. So let me give you an example from the psyllium project. One of our users is Bloomberg. um they actually talked at Psyllium Con here 3 years ago and obviously financial services company what they're trying to do is care about um security and compliance. So, one of Psyllium's features that they have, we have the user Bloomberg.

The feature uh that they're trying to use is network policy to secure their Kubernetes clusters. And specifically, Selium

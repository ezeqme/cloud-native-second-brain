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
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Kat Cosgrove", "Minimus", "Sreeram Venkitesh", "Rayan Das", "DigitalOcean", "Subhasmita Swain", "Independent"]
sched_url: https://kccnceu2026.sched.com/event/2EF5h/the-kep-lifecycle-how-the-release-team-guides-enhancements-to-stability-kat-cosgrove-minimus-sreeram-venkitesh-rayan-das-digitalocean-subhasmita-swain-independent
youtube_search_url: https://www.youtube.com/results?search_query=The+KEP+Lifecycle%3A+How+the+Release+Team+Guides+Enhancements+To+Stability+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The KEP Lifecycle: How the Release Team Guides Enhancements To Stability - Kat Cosgrove, Minimus; Sreeram Venkitesh & Rayan Das, DigitalOcean; Subhasmita Swain, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kat Cosgrove, Minimus, Sreeram Venkitesh, Rayan Das, DigitalOcean, Subhasmita Swain, Independent
- Schedule: https://kccnceu2026.sched.com/event/2EF5h/the-kep-lifecycle-how-the-release-team-guides-enhancements-to-stability-kat-cosgrove-minimus-sreeram-venkitesh-rayan-das-digitalocean-subhasmita-swain-independent
- Busca YouTube: https://www.youtube.com/results?search_query=The+KEP+Lifecycle%3A+How+the+Release+Team+Guides+Enhancements+To+Stability+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The KEP Lifecycle: How the Release Team Guides Enhancements To Stability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5h/the-kep-lifecycle-how-the-release-team-guides-enhancements-to-stability-kat-cosgrove-minimus-sreeram-venkitesh-rayan-das-digitalocean-subhasmita-swain-independent
- YouTube search: https://www.youtube.com/results?search_query=The+KEP+Lifecycle%3A+How+the+Release+Team+Guides+Enhancements+To+Stability+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4if9UBP-NKQ
- YouTube title: The KEP Lifecycle: How the Release Team Guides Enhanceme... Kat C, Sreeram V, Rayan D & Subhasmita S
- Match score: 0.828
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-kep-lifecycle-how-the-release-team-guides-enhancements-to-stabilit/4if9UBP-NKQ.txt
- Transcript chars: 27311
- Keywords: release, enhancements, freeze, process, tracking, feature, basically, already, changes, deadline, actually, questions, features, everything, review, change, tracked, enhancement

### Resumo baseado na transcript

Uh hey folks uh thanks for joining us here today for our talk uh the ke life cycle how to release uh how the release team guides uh enhancements to stability. I am also uh involved with SIG release u release team specifically since uh last two years. So, KB is basically uh Kubernetes uh enhancements proposal uh using which uh the I mean new features and uh deprecations get into uh Kubernetes uh new releases and uh it consists of multiple uh I mean it consists of a design document called uh cap.yamel YML it uh which is basically uh the metadata uh of the ke and uh everything related to the uh enhancements reside inside uh k/ uh enhancements repo and uh let's go over uh Kubernetes release team. So uh the release team basically handles uh everything uh end to end to release uh Kubernetes every uh uh every cycle. We are uh a group of uh people from all over the globe and uh we collaborate and uh bring a new version of Kubernetes to the world every uh uh 15 weeks.

### Excerpt da transcript

Okay. Uh hey folks uh thanks for joining us here today for our talk uh the ke life cycle how to release uh how the release team guides uh enhancements to stability. Uh before that uh a quick round of introduction. My name is Ryan Das. Uh I work at uh Digital Ocean as a senior platform engineer. I am also uh involved with SIG release u release team specifically since uh last two years. And uh this release I am uh uh release uh lead uh shadow and uh yeah. >> Hello everybody. Uh my name is Cat Cosgrove. I am the head of developer advocacy at Minimus but more relevantly for this I'm a member of the Kubernetes steering committee. I own the Kubernetes release team sub project and I'm a technical lead for SIG docs. >> Hey everyone. Uh my name is Freda Madesh. I also work for digital ocean as a senior software engineer in their managed Kubernetes team. I have also been involved with the upstream kubernetes community for a while now. I am part of uh the 136 release team as the release branch management lead and I'm also involved in uh sig node.

>> Hi everyone. Uh my name is Subashmita. I have been around the release team for a quite a long bit like since version 1.26 26 and currently I'm um working as a shadow there like for enhancement sub team and I've been involved in Kubernetes for quite a while uh since my LFX mentorship days working around uh sig cappy uh cappy then capg sub projects so yeah >> yeah thanks everyone so today uh we'll go over uh what caps are uh why we need them And uh we'll go over uh the caps uh point of view of I mean caps uh cap cycle from release team's point of view as well as uh contributors point of view and uh some updates from the uh enhancements uh team. Uh yeah uh what is a ke? So, KB is basically uh Kubernetes uh enhancements proposal uh using which uh the I mean new features and uh deprecations get into uh Kubernetes uh new releases and uh it consists of multiple uh I mean it consists of a design document called uh cap.yamel YML it uh which is basically uh the metadata uh of the ke and uh everything related to the uh enhancements reside inside uh k/ uh enhancements repo and uh let's go over uh Kubernetes release team.

So uh the release team basically handles uh everything uh end to end to release uh Kubernetes every uh uh every cycle. We are uh a group of uh people from all over the globe and uh we collaborate and uh bring a new version of Kubernetes to the world every uh uh 15 weeks. So let's go over the history of CAPS. Uh so

---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Florian Forster", "GitLab"]
sched_url: https://kccnceu2026.sched.com/event/2CW50/building-a-kubernetes-platform-that-scales-from-saas-to-self-managed-florian-forster-gitlab
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Kubernetes+Platform+That+Scales+From+SaaS+To+Self-Managed+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Building a Kubernetes Platform That Scales From SaaS To Self-Managed - Florian Forster, GitLab

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Florian Forster, GitLab
- Schedule: https://kccnceu2026.sched.com/event/2CW50/building-a-kubernetes-platform-that-scales-from-saas-to-self-managed-florian-forster-gitlab
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Kubernetes+Platform+That+Scales+From+SaaS+To+Self-Managed+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Building a Kubernetes Platform That Scales From SaaS To Self-Managed.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW50/building-a-kubernetes-platform-that-scales-from-saas-to-self-managed-florian-forster-gitlab
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Kubernetes+Platform+That+Scales+From+SaaS+To+Self-Managed+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vjF8HjM76wA
- YouTube title: Building a Kubernetes Platform That Scales From SaaS To Self-Managed - Florian Forster, GitLab
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/building-a-kubernetes-platform-that-scales-from-saas-to-self-managed/vjF8HjM76wA.txt
- Transcript chars: 22667
- Keywords: gitlab, self-managed, customers, everything, offering, deploy, platform, single, runway, gitlab.com, satellite, complexity, essentially, production, monolith, release, internal, engineers

### Resumo baseado na transcript

At any rate, um I'm here today to talk to you about how GitLab builds a platform that scales from a single self-managed installation or single node self-managed installation to GitLab's uh ser uh software as a service offering. So by a quick show of hands, who of you is running vendored software in production? At the moment the monolith bundles a bunch of things together that want to scale independently or that want to release independently. And so we need to um need to solve this because in the past we essentially made this vendor lock in decision for us and now it's kind of we we by uh handing uh this the software to our self-managed customer we would would make it their problem. So well why Kubernetes is probably not something I need to evangelize here but we landed on Kubernetes as kind of the common platform uh to to run the the SAS offering as well as to to kind of help our self-managed customers run things. Uh you can use or the our vision is that you can install GitLab on GKE on EKS on your homegrown Kubernetes uh setup in in your home lab uh or in in our development environments.

### Excerpt da transcript

Thank you all for coming here. I know it's late. I'll be your final boss tonight. I'm standing between you and a beer presumably or the end of your day. At any rate, um I'm here today to talk to you about how GitLab builds a platform that scales from a single self-managed installation or single node self-managed installation to GitLab's uh ser uh software as a service offering. So by a quick show of hands, who of you is running vendored software in production? By that I mean somebody else is selling it, you run it. Okay, that's I'd say a majority of the room of those. How many of you are running GitLab? That's appears to be the same number of hands. This is for you. This is good. So little bit about me. My name is Florian. I work as an SRE in the platform team at GitLab and uh I'm the tech lead for uh the runway project and I'm trying to solve this this big scaling problem. So a little bit about GitLab. GitLab is built around a relatively large one of the largest Ruby and Rail code bases uh that exists which we lovingly call our monolith.

Um this monolith get is operated by GitLab itself as a uh software as a service offering. So you can go to gitlab.com uh and buy a repository or buy an organization uh or you can uh buy this as a self-managed instance and then you get to set it up and run it yourself on your local uh hardware. This monolithic architecture, this Ruby on Rails monolith has served GitLab fairly well and this is why we are where we are at the moment. But it is showing kind of signs of weaknesses uh signs of scalability friction and we need to in order to scale more we need to find something to to move away from that or at least in part move away from this uh monolithic uh architecture. At the moment the monolith bundles a bunch of things together that want to scale independently or that want to release independently. maybe they have different compliance requirements and by bundling it all into a monolith we're really increasing coupling too much for its own good. So runway is what we aim to be the solution to this problem.

Uh it's an internal platform and it was originally um built to deploy services that are kind of around the monith. We we call them uh satellite services. We have about a dozen or so that are currently in production. Uh the the one that kickstarted all of this is a Duo, our AI agent coding thing offering. We're about six engineers in the team. So that is a relatively small team for a platform of that complexity. And so it

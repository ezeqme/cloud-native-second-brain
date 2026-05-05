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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Michael McCune", "Joel Speed", "Red Hat", "Bridget Kromhout", "Microsoft", "Jesse Butler", "AWS", "Bowei Du", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EF68/how-will-customized-kubernetes-distributions-work-for-you-a-discussion-on-options-and-use-cases-michael-mccune-joel-speed-red-hat-bridget-kromhout-microsoft-jesse-butler-aws-bowei-du-google
youtube_search_url: https://www.youtube.com/results?search_query=How+Will+Customized+Kubernetes+Distributions+Work+for+You%3F+a+Discussion+on+Options+and+Use+Cases+CNCF+KubeCon+2026
slides: []
status: parsed
---

# How Will Customized Kubernetes Distributions Work for You? a Discussion on Options and Use Cases - Michael McCune & Joel Speed, Red Hat; Bridget Kromhout, Microsoft; Jesse Butler, AWS; Bowei Du, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michael McCune, Joel Speed, Red Hat, Bridget Kromhout, Microsoft, Jesse Butler, AWS, Bowei Du, Google
- Schedule: https://kccnceu2026.sched.com/event/2EF68/how-will-customized-kubernetes-distributions-work-for-you-a-discussion-on-options-and-use-cases-michael-mccune-joel-speed-red-hat-bridget-kromhout-microsoft-jesse-butler-aws-bowei-du-google
- Busca YouTube: https://www.youtube.com/results?search_query=How+Will+Customized+Kubernetes+Distributions+Work+for+You%3F+a+Discussion+on+Options+and+Use+Cases+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre How Will Customized Kubernetes Distributions Work for You? a Discussion on Options and Use Cases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF68/how-will-customized-kubernetes-distributions-work-for-you-a-discussion-on-options-and-use-cases-michael-mccune-joel-speed-red-hat-bridget-kromhout-microsoft-jesse-butler-aws-bowei-du-google
- YouTube search: https://www.youtube.com/results?search_query=How+Will+Customized+Kubernetes+Distributions+Work+for+You%3F+a+Discussion+on+Options+and+Use+Cases+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UeNxyv4REg0
- YouTube title: How Will Customized Kubernetes Distributions Work... Michael M, Joel S, Bridget K, Jesse B & Bowei D
- Match score: 0.722
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/how-will-customized-kubernetes-distributions-work-for-you-a-discussion/UeNxyv4REg0.txt
- Transcript chars: 36056
- Keywords: distribution, conformance, provider, testing, distributions, cluster, specific, talking, actually, features, looking, optional, interesting, saying, probably, everything, question, opinionated

### Resumo baseado na transcript

Uh this is our panel about customized Kubernetes distributions and how they might help you. Uh I one of the co-chairs of SIG cloud provider and I've been working on uh uh oh got notifications coming up. graphical interfaces that are different there are package management you know these type of things and although there are some commercially available distribution ions of Kubernetes. There isn't really yet a a customizable community curated way to do Kubernetes distributions. It's interesting to talk about distributions because we you know you're thinking like well it's like you know it's going to be different but actually I think one of the key things for Kubernetes distribution at least for me is to have as much standardization as possible amongst all the different platforms that you're deploying on and I think one of the key things is like we want to make sure for example the upstream Kubernetes testing works on all platforms and in a very uniform way and I think

### Excerpt da transcript

Welcome everyone. Uh this is our panel about customized Kubernetes distributions and how they might help you. Um my name is Michael McHune. I'm a software engineer at Red Hat. Uh I one of the co-chairs of SIG cloud provider and I've been working on uh uh oh got notifications coming up. Thank you. Thank you John. Um, yeah, I work on a lot of cloud provider stuff, autoscaling and cluster infrastructure. And so this is kind of a problem that I've been thinking about a lot. >> Uh, hi, I'm Joel. I'm also a software engineer at Red Hat. I'm also a SIG cloud tech lead. Um, yeah, I've been doing lots of cloud stuff for the last sort of five, six years with with Red Hat and the SIG Cloud Group. >> I'm Jesse Butler. I'm a product manager in the EKS team. My voice is shot, I apologize. Um, I'm yeah at AWS now since 2020. Um, I've been in the CNCF and open container space for uh since the start pretty much and uh happy to be here. I'm also a maintainer of the uh the SIGs sub project Crow which is why I'm here. Uh but yeah, thanks.

All right. I'm Bridget Cromhout and I work at Microsoft as a product manager in upstream open source and uh I'm also a co-chair of SIG cloud provider and have been active in a number of other projects in CNCF and you know other SIGs and Kubernetes and uh I'm really excited about our collaboration here. >> I am Bowie. You might have seen me in other contexts as the SIG network uh chair and I'm sort of representing Walter but actually I've done a lot of work in the GCP cloud provider G um I work on GKE. >> Okay. So I think you know many people in this room or in this community are familiar with uh Linux distributions right like Auntu, Debian, Fedora whatever and those experiences bring with them you know certain implicit uh I guess user experiences right there's installation there's graphical interfaces that are different there are package management you know these type of things and although there are some commercially available distribution ions of Kubernetes. There isn't really yet a a customizable community curated way to do Kubernetes distributions.

And I'm curious, what might a Kubernetes distribution look like? What what features might it include out of the box? And what user experiences might you expect if this were a thing? >> I'll take this one. It's interesting to talk about distributions because we you know you're thinking like well it's like you know it's going to be different but actually I think one of the key things for Kuber

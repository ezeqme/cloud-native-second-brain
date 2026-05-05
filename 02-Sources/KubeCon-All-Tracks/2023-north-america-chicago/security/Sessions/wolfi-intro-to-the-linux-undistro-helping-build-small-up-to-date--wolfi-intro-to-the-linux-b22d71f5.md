---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["James Rawlings", "Chainguard"]
sched_url: https://kccncna2023.sched.com/event/1R2w7/wolfi-intro-to-the-linux-undistro-helping-build-small-up-to-date-cve-free-cloud-images-james-rawlings-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=Wolfi%3A+Intro+to+the+Linux+Undistro+Helping+Build+Small%2C+up-to-Date%2C+CVE+Free+Cloud+Images+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Wolfi: Intro to the Linux Undistro Helping Build Small, up-to-Date, CVE Free Cloud Images - James Rawlings, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Chicago
- Speakers: James Rawlings, Chainguard
- Schedule: https://kccncna2023.sched.com/event/1R2w7/wolfi-intro-to-the-linux-undistro-helping-build-small-up-to-date-cve-free-cloud-images-james-rawlings-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=Wolfi%3A+Intro+to+the+Linux+Undistro+Helping+Build+Small%2C+up-to-Date%2C+CVE+Free+Cloud+Images+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Wolfi: Intro to the Linux Undistro Helping Build Small, up-to-Date, CVE Free Cloud Images.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2w7/wolfi-intro-to-the-linux-undistro-helping-build-small-up-to-date-cve-free-cloud-images-james-rawlings-chainguard
- YouTube search: https://www.youtube.com/results?search_query=Wolfi%3A+Intro+to+the+Linux+Undistro+Helping+Build+Small%2C+up-to-Date%2C+CVE+Free+Cloud+Images+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bXkXu_IKVdI
- YouTube title: Wolfi: Intro to the Linux Undistro Helping Build Small, up-to-Date, CVE Free... - James Rawlings
- Match score: 0.965
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/wolfi-intro-to-the-linux-undistro-helping-build-small-up-to-date-cve-f/bXkXu_IKVdI.txt
- Transcript chars: 33072
- Keywords: wolfie, actually, packages, package, version, images, software, around, little, container, vulnerabilities, versions, understand, create, source, upstream, pipeline, created

### Resumo baseado na transcript

hello good afternoon uh thank you all for coming my name is James Rawlings I'm a software engineer working at chainu guard um we've got come here today we're going to have a little talk around Wolfie just before that um I'd like to ponder I Ponder quite a bit ponder about many different things recently I was pondering about Lego Lego is kind of cool I'm always amazed by it um I was trying to understand why I'm so impressed by it and how it kind of became so image we should be able to go Etc demo message this is just demonstrating that we've built um an APK using milange yeah it was a bit there a rubbish message in the middle there don't if you can see that um but the the

### Excerpt da transcript

hello good afternoon uh thank you all for coming my name is James Rawlings I'm a software engineer working at chainu guard um we've got come here today we're going to have a little talk around Wolfie just before that um I'd like to ponder I Ponder quite a bit ponder about many different things recently I was pondering about Lego Lego is kind of cool I'm always amazed by it um I was trying to understand why I'm so impressed by it and how it kind of became so successful so in my head I was whilst I was pondering I was breaking it down um I love Lego because it's all these small composable blocks so you can build together there's all many different shapes and sizes but there's always a contract for how they all fit together so you can take instructions from the object that you're trying to build you can use those instructions to build it or you can get creative and taking all those building blocks and be creative and build your own uh designs yourselves there's tools I don't know if anybody's seen the I mean this wasn't in my age but there's now this orange tool thingy magig I don't know what it's the name of it's called but it's kind of awesome because it helps you be more productive and work better with the Lego and also this is the one thing that I really do love about Lego and when I thinking about it or doing my ponderings that whenever you buy a a package F from Lego you always have just the bits needed to do build the actual object you don't have hundreds of extra pieces lying around adding that complexity making it more complicated it's just the bits needed to do the job okay that was my ponderings I wanted to share that may or may not be appropriate as we go through the rest of the presentation um so Wolfie what is Wolfie well Wolfie is used to build Cloud native images Cloud container images um it's designed specifically for the cloud native era it's a l Linux unisto built using GBC the reason I say the UN the undro is significant because as these are Cloud containers they're running on on the cloud they're actually using the kernel from the host these images don't include the kernel glad you could all turn up thank you very much these chain Guardians um it's also a collection of software packages so there are 1,700 current software packages in Wolfie um and there's continually growing more and more and more they are built with currently built with to run on both arm and x86 as well and we use Alpine's APK packaging format um you can't mix and match

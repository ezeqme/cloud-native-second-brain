---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Jeremy Rickard", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvu/project-lightning-talk-project-copacetic-jeremy-rickard-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Project+Copacetic+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Project Copacetic - Jeremy Rickard, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Jeremy Rickard, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcvu/project-lightning-talk-project-copacetic-jeremy-rickard-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Project+Copacetic+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Project Copacetic.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvu/project-lightning-talk-project-copacetic-jeremy-rickard-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Project+Copacetic+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Q9m7eGoBaMA
- YouTube title: Project Lightning Talk: Project Copacetic - Jeremy Rickard, Maintainer
- Match score: 0.835
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-project-copacetic/Q9m7eGoBaMA.txt
- Transcript chars: 5136
- Keywords: container, images, packages, support, generate, actually, github, multiple, vulnerabilities, scanner, identify, package, scanning, docker, report, number, lightning, copacetic

### Resumo baseado na transcript

So, Copathetic is a tool to directly patch vulnerabilities in container images. Well, it does that by being a uh build kit based CLI tool that knows how to interpret scanner results. If you're going to do it for multiple architectures, you'll also do it multiple times. We'd love to talk to you, give you some demos and and answer any questions you have.

### Excerpt da transcript

All right. Uh, hey everybody. Thanks for coming to uh, the project copacetic lightning talk. Uh, quick show of hands. Who likes CVEes in container images? Who does not like CVS in container images? Wow. I said I asked the question wrong. All right. So, Copathetic is a tool to directly patch vulnerabilities in container images. How does it do that? Well, it does that by being a uh build kit based CLI tool that knows how to interpret scanner results. So something like trivy or gripe. Uh identify vulnerable packages within those reports. Um use the package managers for the underlying distribution for the container. Generate a new patch layer and apply that on top of the existing container. And it can do this without actually having the tooling in the container. So if you have a DR list container, for example, uh Copa is actually able to patch that. Um Copa is a CNCF sandbox project. Uh you can go check it out today. I'll have a link to the GitHub repo at the end. Um and it's uh it's pretty easy to get going with.

Uh by default, Copa uses uh the Trivy uh scanning software, but it also supports pluggable scanner. So Gripe is one. Docker Scout is also available. uh if you have another tool that you're interested in, we would totally like to have community contributions for those things. So, how does Copa actually work? Well, there's two modes that you can use Copa with. Um the first is what I just mentioned where you're going to use a vulnerability uh scanning tool like Trivy to be able to identify vulnerabilities that are in the project. But Copa can actually work without that and just scan the container um for any updated packages that exist in the package manager for the underlying OS. Let's let's say it's going to be Ubuntu um and and just install all package updates. Maybe a little less surgical than taking a scan report and and going with that. But maybe it's a a good use case for you. So what typically would happen here is that you would generate a vulnerability report using triva. So number two, copa would parse that identify all the vulnerabilities uh and then take those things and look for new packages that are available.

Then using build kit under the covers, it's going to generate a new um file system layer using the old image uh layers together. It will then use uh you know if it's going to be an RPM based system, it'll use RPM. If it's a buntu, it'll use deb or appget uh and install those updated packages into that new file system layer and then

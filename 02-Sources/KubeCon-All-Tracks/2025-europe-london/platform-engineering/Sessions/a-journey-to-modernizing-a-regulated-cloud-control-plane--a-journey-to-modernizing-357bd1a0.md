---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Pranita Praveen", "Macquarie Group Pty Ltd", "Steven Borrelli", "Upbound"]
sched_url: https://kccnceu2025.sched.com/event/1txB9/a-journey-to-modernizing-a-regulated-cloud-control-plane-pranita-praveen-macquarie-group-pty-ltd-steven-borrelli-upbound
youtube_search_url: https://www.youtube.com/results?search_query=A+Journey+To+Modernizing+a+Regulated+Cloud+Control+Plane+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Journey To Modernizing a Regulated Cloud Control Plane - Pranita Praveen, Macquarie Group Pty Ltd & Steven Borrelli, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Pranita Praveen, Macquarie Group Pty Ltd, Steven Borrelli, Upbound
- Schedule: https://kccnceu2025.sched.com/event/1txB9/a-journey-to-modernizing-a-regulated-cloud-control-plane-pranita-praveen-macquarie-group-pty-ltd-steven-borrelli-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=A+Journey+To+Modernizing+a+Regulated+Cloud+Control+Plane+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Journey To Modernizing a Regulated Cloud Control Plane.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txB9/a-journey-to-modernizing-a-regulated-cloud-control-plane-pranita-praveen-macquarie-group-pty-ltd-steven-borrelli-upbound
- YouTube search: https://www.youtube.com/results?search_query=A+Journey+To+Modernizing+a+Regulated+Cloud+Control+Plane+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TELnK0PrKHU
- YouTube title: A Journey To Modernizing a Regulated Cloud Control Plane - Pranita Praveen & Steven Borrelli
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-journey-to-modernizing-a-regulated-cloud-control-plane/TELnK0PrKHU.txt
- Transcript chars: 25204
- Keywords: crossplane, control, resources, request, wanted, developers, platform, argo, pipeline, everything, engineers, deployment, security, composition, faster, existing, mcquaryy, experience

### Resumo baseado na transcript

Uh we'll be talking about the um the journey to evolving our cloud control plane in Mcquaryy group. I've got a bit of experience in platform engineering in cloud platforms essentially. So in McCory, we're highly regulated and when we want to consume a new cloud service for development and test, we need to make sure that we've got some security boundaries and guardrails around that service. Um today we have probably one of the most popular control planes on the platin and kubernetes. key technologies within kubernetes and use it to make a universal control plane uh can we manage everything with kubernetes um and what crossplane does is it's an extension to kubernetes and it uses core technologies like cds custom resource definitions and controllers and he uses that to expand extend Kubernetes reach to be able to manage almost anything.

### Excerpt da transcript

Hi everyone, nice to meet you. Thanks for coming to our talk today. Uh we'll be talking about the um the journey to evolving our cloud control plane in Mcquaryy group. I'm Prrenita Praine and I'm a director of engineering in Mcquaryy. I've got a bit of experience in platform engineering in cloud platforms essentially. That's my background for the past 10 years. I'll be presenting with Steven. Hello. Yes, I'm Steven Purley, a principal solutions architect at Upbound and a member of the crossplane community. So, just a little bit about Mcquaryy if you don't know already. So, at Mcquaryy, we're a financial services group. So, we provide asset management, investment banking, retail banking services. We're headquartered in Sydney, Australia, but we are global. So, we've got an office in London, um all all around the world really in Americas as well. Uh I'm based in Melbourne. Um, so it's a pretty fun place to work in. There's about 20,000 or so um, employees, so fairly big for a company. Uh, we really love to say that, you know, we're empowering our people, both our staff as well as our customers to innovate and invest for a better future.

Um, in saying that, about 10 years ago, we started uh uh moving all our tech stack onto the public cloud. We started with AWS and now eventually we've gotten on to GCP as well as Microsoft Azure. So we're firmly multicloud right now. I would say we're about 70% or more at least in the public cloud and we're still looking at moving some of our old stack into the public cloud because we started quite a while ago. Um we're mostly I is right now and mostly sitting in AWS but we are looking to uplift that move on to pads and SAS solutions. um and also become more more firmly multicloud as well with the proper strategy. We found that over the 10 years because we've just been focused on moving all of our stuff into the cloud etc. Um our pipeline that we'd used to get onto the cloud was uh getting more and more cumbersome to maintain. Um we were finding that there was a bit more toil for the platform engineers in fixing um what we needed to fix to get it working to support our production applications. Um and we also had because we started with AWS moved on to GCP Azure we had different solutions for deployment into the three clouds.

So that was a little bit more operations um heavy. We wanted just one multi cloud solution. Um so then we started thinking about how do we change this? What do we want to do to uplift what we're doing i

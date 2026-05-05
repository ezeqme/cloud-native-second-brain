---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Keynote Sessions"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Brenda Chan", "Director of Engineering", "VMware Tanzu Developer Experience", "VMware"]
sched_url: https://kccnceu2021.sched.com/event/ijH0/sponsored-keynote-smoothing-the-onramp-to-kubernetes-with-knative-brenda-chan-director-of-engineering-vmware-tanzu-developer-experience-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Smoothing+the+onramp+to+Kubernetes+with+Knative+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Keynote: Smoothing the onramp to Kubernetes with Knative - Brenda Chan, Director of Engineering, VMware Tanzu Developer Experience, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Brenda Chan, Director of Engineering, VMware Tanzu Developer Experience, VMware
- Schedule: https://kccnceu2021.sched.com/event/ijH0/sponsored-keynote-smoothing-the-onramp-to-kubernetes-with-knative-brenda-chan-director-of-engineering-vmware-tanzu-developer-experience-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Smoothing+the+onramp+to+Kubernetes+with+Knative+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Smoothing the onramp to Kubernetes with Knative.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/ijH0/sponsored-keynote-smoothing-the-onramp-to-kubernetes-with-knative-brenda-chan-director-of-engineering-vmware-tanzu-developer-experience-vmware
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Smoothing+the+onramp+to+Kubernetes+with+Knative+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iMMe41x5mGE
- YouTube title: Sponsored Keynote: Smoothing the onramp to Kubernetes with Knative - Brenda Chan, Director
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-keynote-smoothing-the-onramp-to-kubernetes-with-knative/iMMe41x5mGE.txt
- Transcript chars: 4321
- Keywords: k-native, everyone, actually, committee, create, deployment, update, steering, towards, awesome, probably, ingress, vmware, experience, conformance, extremely, pretty, deploying

### Resumo baseado na transcript

[Music] hi everyone i'm here today to talk about spooning the on-ramp to kubernetes with k-native so just a quick introduction for everyone here my name is brenda chan i'm located in toronto canada uh my current role at vmware is the engineering director for vmware tons of developer experience however within the k-native community i've been on the steering committee since the bootstrap phase in 2019 during my time on steering we've worked towards a completely community elected technical oversight committee or toc in steering committee in october 2020

### Excerpt da transcript

[Music] hi everyone i'm here today to talk about spooning the on-ramp to kubernetes with k-native so just a quick introduction for everyone here my name is brenda chan i'm located in toronto canada uh my current role at vmware is the engineering director for vmware tons of developer experience however within the k-native community i've been on the steering committee since the bootstrap phase in 2019 during my time on steering we've worked towards a completely community elected technical oversight committee or toc in steering committee in october 2020 we formed the trademark committee and one really neat thing we're focusing on right now is actually defining k-native conformance and working towards a set of conformance test suites for when we plan to 1.0 this year so kubernetes is awesome i probably don't need to say more than that since we are at kubecon after all but really kubernetes has allowed us to normalize our infrastructure abstractions we have a thriving ecosystem in large community thank you for all of those who are actually here today and honestly kubernetes extensibility has proven to be extremely valuable and powerful the thing is is that kubernetes can actually be pretty hard in the cncf survey report in 2020 to the question what are your challenges in using in deploying containers the main challenge that the respondents actually replied with was that it was complex and i'd really like to spend some time today to explore that because it really doesn't need to be that hard so let's actually try this out let's run a stateless web server so you have me there on the left the the kubernetes engineer with 20 years of experience so first you'll want to create a deployment object you open up them you create some yaml make sure your indentation looks good great youtube cut i'll apply the deployment so far so good all right so now you create a kubernetes service uh you specify the port ensure you're targeting the right app and again you could apply that so now you need to make sure you can route traffic to your service so let's create an ingress uh ensure you have the right service name and port you could all apply that awesome and you're happy and this is awesome because it just works but let's do this again you may need to update something maybe the image change the port changed who knows so again you go through the same thing you update your deployment animal keep it will apply you may update the service coupe codon apply update the ingress keep it'

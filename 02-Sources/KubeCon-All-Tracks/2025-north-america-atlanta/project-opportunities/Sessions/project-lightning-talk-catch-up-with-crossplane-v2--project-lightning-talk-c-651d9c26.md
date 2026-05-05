---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["Community Governance"]
speakers: ["Scott Rosenberg", "Contributor"]
sched_url: https://kccncna2025.sched.com/event/27d59/project-lightning-talk-catch-up-with-crossplane-v2-scott-rosenberg-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Catch+Up+With+Crossplane+v2+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Catch Up With Crossplane v2 - Scott Rosenberg, Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Scott Rosenberg, Contributor
- Schedule: https://kccncna2025.sched.com/event/27d59/project-lightning-talk-catch-up-with-crossplane-v2-scott-rosenberg-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Catch+Up+With+Crossplane+v2+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Catch Up With Crossplane v2.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d59/project-lightning-talk-catch-up-with-crossplane-v2-scott-rosenberg-contributor
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Catch+Up+With+Crossplane+v2+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mr_zhO2lV2w
- YouTube title: Project Lightning Talk: Catch Up With Crossplane v2 - Scott Rosenberg, Contributor
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-catch-up-with-crossplane-v2/mr_zhO2lV2w.txt
- Transcript chars: 6976
- Keywords: crossplane, providers, resources, cluster, provider, resource, control, allows, created, terraform, everything, basically, scoped, managed, extremely, powerful, compose, composition

### Resumo baseado na transcript

Hey everyone and uh today we're going to talk about crossplane v2 the new major version of crossplane. So my name is Scott Rosenberg global SI uh I'm the lead architect in the CT office at Terra Sky. So this caused a bunch of challenges and the claim tox you know kind of conversion and mapping just caused a bunch of excessive complexity and if we take a look at what crossplane v2 does we've greatly simplified this we now have the composite things like that and there was no direct for non there was no direct support for non-crossplane managed resources that means I needed to use these wrapper providers the Kubernetes provider or the helm provider all these different providers to allow me just to create a deployment in Kubernetes um which made it way more complex than it needed to be in many cases and this is where in crossplane v2 we have a way less opinionated stack which allows us to compose any resource out of a composition this certain cloud providers starting with G uh you know it could crash their API servers often uh when you would install certain providers just the amount of CRDs until it would come back up and scale automatically and we had challenges with this.

### Excerpt da transcript

Hey everyone and uh today we're going to talk about crossplane v2 the new major version of crossplane. So my name is Scott Rosenberg global SI uh I'm the lead architect in the CT office at Terra Sky. Um and let's talk about crossplane. So quick overview what is crossplane right crossplane is the cloudnative control plane. It really allows us to provide to provision to manage all of our resources. It brings the paradigm of Kubernetes to everything basically um making it extremely powerful. One of the great capabilities we can do is we can actually compose a lot of resources together using this idea of an XRD and a composition where we can define an API and then compose together all of our resources into userfacing APIs that really make sense for our end users. Um and this allows us to offer self-service for our end users. Now, Kubernetes is an amazing control plane for containers as mentioned and really crossplane is how do I extend that out to basically anything that has an API be that the public cloud be that vSphere or cubevert or any onrem solution be that a graphana dashboard really whatever we want um the methodology of control planes has existed for years in the cloud providers what crossplane is doing is democratizing that and giving all of us the capability to build that control plane oursel.

So when we talk about building our own platform API in crossplane v1 um we had this idea of our XRD right which is our definition that's my API from there that created two different resources for us that created a claim and which was a namespace scoped API resource and then we had the cluster scope that was basically a mirroring of one another. um you created a claim that created in the back end automatically the cluster scoped XR. An XRD has one or more implementations of that interface which are called compositions. A composition comes and is picked up by the XR and we get a bunch of managed resources that get deployed. An RDS instance, a DB subnet, a security group, right? Obviously, if this was really AWS, we would be talking somewhere around 70 to 80 actual resources to create an RDS instance, but that's a whole another story. Now, when we actually look at how this works, the claim is namespace scoped. Everything else is cluster scoped. And this really brought a bunch of complexity to it. We had number one the cluster scope managed resources which was really kind of modeled after the idea of a persistent volume and a persistent volume claim.

But this ca

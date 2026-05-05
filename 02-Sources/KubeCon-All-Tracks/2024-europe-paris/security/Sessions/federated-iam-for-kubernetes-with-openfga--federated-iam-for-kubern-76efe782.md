---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Jonathan Whitaker", "Okta"]
sched_url: https://kccnceu2024.sched.com/event/1YeQD/federated-iam-for-kubernetes-with-openfga-jonathan-whitaker-okta
youtube_search_url: https://www.youtube.com/results?search_query=Federated+IAM+for+Kubernetes+with+OpenFGA+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Federated IAM for Kubernetes with OpenFGA - Jonathan Whitaker, Okta

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Jonathan Whitaker, Okta
- Schedule: https://kccnceu2024.sched.com/event/1YeQD/federated-iam-for-kubernetes-with-openfga-jonathan-whitaker-okta
- Busca YouTube: https://www.youtube.com/results?search_query=Federated+IAM+for+Kubernetes+with+OpenFGA+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Federated IAM for Kubernetes with OpenFGA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQD/federated-iam-for-kubernetes-with-openfga-jonathan-whitaker-okta
- YouTube search: https://www.youtube.com/results?search_query=Federated+IAM+for+Kubernetes+with+OpenFGA+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UaK1EnRgrng
- YouTube title: Federated IAM for Kubernetes with OpenFGA - Jonathan Whitaker, Okta
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/federated-iam-for-kubernetes-with-openfga/UaK1EnRgrng.txt
- Transcript chars: 32341
- Keywords: access, policies, identity, keycloak, authorization, control, cluster, relationship, provider, called, policy, resources, binding, across, actually, temporal, resource, applications

### Resumo baseado na transcript

so my name is Jonathan Whitaker I am a staff software engineer at OCTA and ozero and I'm also a core maintainer of the open fga project today I'm going to be talking with you all about Federated identity and access management for kubernetes with open fga and we will use keycloak in this example as well to represent an identity provider uh as we demonstrate this Federation so to kick things off let's just start with some simple definitions um it's often overlooked what is Federation so the web to our kubernetes cluster here's an example manifest for some rback resources we're going to create a namespace called fga backend and in that Nam space we will create a role called deployment reader that will allow the get and list verbs on deployments and an incognito browser so we get a fresh session and everything and I'll log in with John Whitaker oo.com that's my password we've authenticated now against our kubernetes cluster if we go back to our terminal we can see that we got an unauthorized response from the cube API server this user with this ID cannot list the deployment resource in the fga backend namespace that was forbidden so let's go back into our kubernetes Administration console and we will go to users go here and we will add John

### Excerpt da transcript

so my name is Jonathan Whitaker I am a staff software engineer at OCTA and ozero and I'm also a core maintainer of the open fga project today I'm going to be talking with you all about Federated identity and access management for kubernetes with open fga and we will use keycloak in this example as well to represent an identity provider uh as we demonstrate this Federation so to kick things off let's just start with some simple definitions um it's often overlooked what is Federation so the web services F uh web services Federation spec defines Federation as the allowance of security principal identities and attributes to be shared across trust boundaries according to established policies so what does that really mean right we have we have this stack we have infrastructure we have applications you know we have identity providers we have a lot of security context and it's spread across ious applications and and infrastructure in our ecosystem and in order to ask you know Access Control decisions and to answer you know certain policies we need to be able to share that context across these boundaries and we need to be able to do so so that we can evaluate these policies across these different contexts now in Industry today we have focused a lot in the last 10 to 15 years on identity Federation and directory services so some of the existing standards and protocols for the Federation of identity specifically these include things like open ID connect uh oath 2 saml 2 and the web services Federation spec I'm sure all of you are probably aware with some of these um You probably use them in your day-to-day job right now this is where we've largely been focused in the industry again over the last 10 to 15 years we've been focused on the identity management piece of the identity and access management pi and I would argue that as an industry we have yet to cohesively stitch together the access management side of the identity access and access management puzzle so I'd like to see more development you know as a community and as an industry in this space stitching these two things together more cohesively so I'm going to pose a question to the community to all of us today what if identity and access management was actually identity and you know underscore the and part access management if only we could if only we could start to establish some standards or protocols uh maybe you know apis for enforcing access controls across trust boundaries right this Federation that we're

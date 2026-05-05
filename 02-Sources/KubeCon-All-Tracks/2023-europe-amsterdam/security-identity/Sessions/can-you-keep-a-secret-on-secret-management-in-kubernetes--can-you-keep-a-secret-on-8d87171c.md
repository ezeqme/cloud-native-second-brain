---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Kubernetes Core"]
speakers: ["Liav Yona", "Gal Cohen", "Firefly"]
sched_url: https://kccnceu2023.sched.com/event/1HyY5/can-you-keep-a-secret-on-secret-management-in-kubernetes-liav-yona-gal-cohen-firefly
youtube_search_url: https://www.youtube.com/results?search_query=Can+You+Keep+a+Secret%3F+on+Secret+Management+in+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Can You Keep a Secret? on Secret Management in Kubernetes - Liav Yona & Gal Cohen, Firefly

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Liav Yona, Gal Cohen, Firefly
- Schedule: https://kccnceu2023.sched.com/event/1HyY5/can-you-keep-a-secret-on-secret-management-in-kubernetes-liav-yona-gal-cohen-firefly
- Busca YouTube: https://www.youtube.com/results?search_query=Can+You+Keep+a+Secret%3F+on+Secret+Management+in+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Can You Keep a Secret? on Secret Management in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyY5/can-you-keep-a-secret-on-secret-management-in-kubernetes-liav-yona-gal-cohen-firefly
- YouTube search: https://www.youtube.com/results?search_query=Can+You+Keep+a+Secret%3F+on+Secret+Management+in+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UHbEL1n7fqw
- YouTube title: Can You Keep a Secret? On Secret Management in Kubernetes by Gal Cohen and Liav Yona
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/can-you-keep-a-secret-on-secret-management-in-kubernetes/UHbEL1n7fqw.txt
- Transcript chars: 16053
- Keywords: secret, secrets, provider, external, solution, cluster, access, application, driver, manage, source, volume, component, infrastructure, applications, sensitive, create, manager

### Resumo baseado na transcript

hey everyone hello from Israel we are super excited to be today and talk with you about kubernetes secrets we had a lot of experience working with kubernetes secrets and we want to show you what we've learned and about how they work in Real World Systems and the best solution to manage them but before we Dive In a background about Who We Are I'm gal I'm backing engineer at Firefly in my day job I'm responsible for large-scale kubernetes application and I'm passionate about kubernetes Concepts hi I'm

### Excerpt da transcript

hey everyone hello from Israel we are super excited to be today and talk with you about kubernetes secrets we had a lot of experience working with kubernetes secrets and we want to show you what we've learned and about how they work in Real World Systems and the best solution to manage them but before we Dive In a background about Who We Are I'm gal I'm backing engineer at Firefly in my day job I'm responsible for large-scale kubernetes application and I'm passionate about kubernetes Concepts hi I'm Leah I'm an engineering team lead at Firefly as well I recently had the privilege of speaking about migrating from Lambda function to kubernetes job at community kubernetes community days Amsterdam and I'm super excited to have this opportunity to share with you what we have learned on our journey with kubernetes secrets so let's begin yeah just a second yesterday it just hit me that yesterday I deployed a new service in production cluster that uses mongodb database and they put the manga the big credentials as a kubernetes secret as you know girl that's not the most secure solution out there it's actually not encrypted at all wow then I guess we need to think about our options for changing this finally that's exactly what I'm planning to uncovering in this talk so here we go I forever question the security level of your organization secrets when I'm saying secret I'm referring to database passwords service access tokens private keys all those secrets that all that all your applications rely on and all your customer sensitive data being protected with well we did we did it because of the importance of our clients and our very own sensitive data and I think that and we think that everyone should do so so today we'll share with you everything you need to know about safe secret Management in kubernetes we will go through the Technologies and tools that help us manage secrets in a secure way and we will wrap up with a live demo for how to use kubernetes Secret store CSI driver first things first before we get we started with all that what is the secret a secret is an object that contains sensitive data like an access key token or password as developer we use them all the time like for tick tock account but not just that but really a more commonly commonly usage of Secrets within our application is in order to connect to a database authenticate to third-party services decrypt a message and much more these are just a few examples this is because secrets are essential

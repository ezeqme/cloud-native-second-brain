---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Alessio Greggi", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxA/project-lightning-talk-blocking-vulnerable-workloads-out-and-catching-what-got-in-alessio-greggi-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Blocking+Vulnerable+Workloads+Out+%28And+Catching+What+Got+In%29+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Blocking Vulnerable Workloads Out (And Catching What Got In) - Alessio Greggi, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alessio Greggi, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxA/project-lightning-talk-blocking-vulnerable-workloads-out-and-catching-what-got-in-alessio-greggi-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Blocking+Vulnerable+Workloads+Out+%28And+Catching+What+Got+In%29+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Blocking Vulnerable Workloads Out (And Catching What Got In).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxA/project-lightning-talk-blocking-vulnerable-workloads-out-and-catching-what-got-in-alessio-greggi-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Blocking+Vulnerable+Workloads+Out+%28And+Catching+What+Got+In%29+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0ItI-HaO7do
- YouTube title: Project Lightning Talk: Blocking Vulnerable Workloads Out (And Catching What Got I... Alessio Greggi
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-blocking-vulnerable-workloads-out-and-catching/0ItI-HaO7do.txt
- Transcript chars: 3801
- Keywords: policy, basically, registry, scanner, vulnerability, report, warden, vulnerabilities, inside, cluster, integration, number, favorite, general, images, applying, resource, vulnerable

### Resumo baseado na transcript

My name is Alessio and today I'm going to show you nice integration that we made using a new policy for Cube Warden to block workloads that have a specified number of CV that we want to block. Um Its particularity is that you can write your own policies you using your favorite language since Cube Warden provides the SDK for several languages.

### Excerpt da transcript

Welcome everyone. My name is Alessio and today I'm going to show you nice integration that we made using a new policy for Cube Warden to block workloads that have a specified number of CV that we want to block. So let's start by introducing what Cube Warden is. So it's a universal policy engine. Um Its particularity is that you can write your own policies you using your favorite language since Cube Warden provides the SDK for several languages. You can use for example go or rust, typescript and so on and so forth. And the nice thing is that you can basically compile the policies with your favorite language into an OCI artifact thanks to Wasm. So you basically have this single binary and you can push this on your favorite registry. So that you can eat available for the policy that you that you need. The other component which is a part of this integration is a SBOM scanner. So SBOM scanner is a a new component of the Cube Warden project and it's basically an SBOM centric security scanner. We are actually using Trivy under the hood but we plan to extend the support for other scanners so that the vulnerability report will be enriched by all of them.

In general you can basically configure a registry so that SBOM scanner will point to that registry and scan for the images inside the registry. Of course you can use some filters to avoid scanning the whole registry if you don't need the entire posture but in general it works with a this CRD which is the registry one and it basically produce as a result vulnerability report of all the images that have been scanned on the registry. So you can see all the vulnerabilities that are affecting your images inside the registry that you configured. Now the integration is about this new policy that we made by combining Cube Warden and SBOM scanner. So their their potential all together. And the policy is the image CV policy. So it basically enforce maximum number of vulnerabilities inside an image before to get applied on your cluster. So if you want to avoid having like vulnerable CVs inside your cluster you can basically avoid it when you are applying the the resource. So the policy is a context aware policy as I said so it needs information coming from from from SBOM scanner which is the vulnerability report CRD.

So let's see how can you apply this. So to apply the the policy you you need a cluster administration policy. And you can see the pointer. Okay. So you basically recall the policy using the module attribute. So

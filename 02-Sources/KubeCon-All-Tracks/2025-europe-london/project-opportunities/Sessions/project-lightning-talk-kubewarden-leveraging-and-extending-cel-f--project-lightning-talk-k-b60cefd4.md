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
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Robert Sirchia", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcub/project-lightning-talk-kubewarden-leveraging-and-extending-cel-for-your-cluster-security-robert-sirchia-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubewarden%3A+Leveraging+and+Extending+CEL+for+your+Cluster+Security+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Kubewarden: Leveraging and Extending CEL for your Cluster Security - Robert Sirchia, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Robert Sirchia, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcub/project-lightning-talk-kubewarden-leveraging-and-extending-cel-for-your-cluster-security-robert-sirchia-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubewarden%3A+Leveraging+and+Extending+CEL+for+your+Cluster+Security+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Kubewarden: Leveraging and Extending CEL for your Cluster Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcub/project-lightning-talk-kubewarden-leveraging-and-extending-cel-for-your-cluster-security-robert-sirchia-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubewarden%3A+Leveraging+and+Extending+CEL+for+your+Cluster+Security+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l3mSvnpLGZY
- YouTube title: Project Lightning Talk: Kubewarden: Leveraging and Extending CEL for your Cluster... Robert Sirchia
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-kubewarden-leveraging-and-extending-cel-for-you/l3mSvnpLGZY.txt
- Transcript chars: 3141
- Keywords: policies, policy, kuborton, language, extending, cluster, talking, within, write, actually, leveraging, security, domain, specific, designed, embedded, compiled, assembly

### Resumo baseado na transcript

My talk quickly today is Kuborton leveraging and extending CEL for your cluster security. I am a Helm maintainer and I'm talking not about Helm, I'm talking about Kuborton and I'm talking about CEL. Um plus Kubort and host of opportunities when gives you the when you expand when you expose into native cell right so you can gain access to kubernetes resources six verification OCI registries network queries things like that and since it's couparden you have a

### Excerpt da transcript

My talk quickly today is Kuborton leveraging and extending CEL for your cluster security. Real quick, my name is Robert Suchia. I am a Helm maintainer and I'm talking not about Helm, I'm talking about Kuborton and I'm talking about CEL. I'm a CNCF ambassador and I'm a director in the office of the CTO for a company called SUSA if you heard of it. But let's get into it. Um, common expression language. This is a domain specific language. It's already within um Kubernetes right now with the validating ad uh admission policies. It's ideal for extending declarative configurations. Um it's fast, it's portable, it's safe to execute. Um it provides a Kubernetes lang language feature as well. Um and it's designed to be embedded, right? But it can run on its own and it can be compiled into WASM. So I couldn't ask for a better setup than I got with the previous speaker. So thank you if he's still here. So what is Kuborton? Kuborton is a CNCF project. It's a sandbox project. We talked about where it's at in its maturity.

It is a policy engines whose policies are built in web assembly modules. So if you like web assembly, you like policies, it's kind of a project built for you. You can write your own policies choosing your own languages. Um your domain specific languages such as Cell or RIO. Um, you'll use a general purpose language such as Go, Rust, uh, C#, JavaScript. We have SDKs to cover all of that. And we actually have documentation so you can actually run and write your own policies. But we do recommend that you first um, check out what policies we have in ArtifactHub before you write your own. And it's designed to protect your clusters. You can gain insight and you can build modular solutions that run. Um and we're striving to be a universal policy engine. So it is a supererset of Kubernetes Cell straight from the source. Um it uses the same upstream cell interpreter um the same add-ons and libraries into cell compiled into cell policies. It's backwards compatible with cell as well. Um plus Kubort and host of opportunities when gives you the when you expand when you expose into native cell right so you can gain access to kubernetes resources six verification OCI registries network queries things like that and since it's couparden you have a lot of extra features in there um the process of re recoccurring cluster information resources etc with that.

So a quick example what this would look like if you were deploying a particular policy, you can have the opportu

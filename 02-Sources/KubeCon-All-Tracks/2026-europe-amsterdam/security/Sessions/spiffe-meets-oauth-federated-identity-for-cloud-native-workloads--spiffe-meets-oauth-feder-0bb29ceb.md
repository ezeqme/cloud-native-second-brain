---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security"]
speakers: ["Yoshiyuki Tabata", "Hitachi", "Ltd."]
sched_url: https://kccnceu2026.sched.com/event/2CW5g/spiffe-meets-oauth-federated-identity-for-cloud-native-workloads-yoshiyuki-tabata-hitachi-ltd
youtube_search_url: https://www.youtube.com/results?search_query=SPIFFE+Meets+OAuth%3A+Federated+Identity+for+Cloud+Native+Workloads+CNCF+KubeCon+2026
slides: []
status: parsed
---

# SPIFFE Meets OAuth: Federated Identity for Cloud Native Workloads - Yoshiyuki Tabata, Hitachi, Ltd.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yoshiyuki Tabata, Hitachi, Ltd.
- Schedule: https://kccnceu2026.sched.com/event/2CW5g/spiffe-meets-oauth-federated-identity-for-cloud-native-workloads-yoshiyuki-tabata-hitachi-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=SPIFFE+Meets+OAuth%3A+Federated+Identity+for+Cloud+Native+Workloads+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre SPIFFE Meets OAuth: Federated Identity for Cloud Native Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5g/spiffe-meets-oauth-federated-identity-for-cloud-native-workloads-yoshiyuki-tabata-hitachi-ltd
- YouTube search: https://www.youtube.com/results?search_query=SPIFFE+Meets+OAuth%3A+Federated+Identity+for+Cloud+Native+Workloads+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_qVWLU2sLnw
- YouTube title: SPIFFE Meets OAuth: Federated Identity for Cloud Native Workloads - Yoshiyuki Tabata, Hitachi, Ltd.
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/spiffe-meets-oauth-federated-identity-for-cloud-native-workloads/_qVWLU2sLnw.txt
- Transcript chars: 18457
- Keywords: authorization, server, identity, spiffy, domain, access, client, sample, request, domains, authentication, across, workload, exchange, introspection, federated, implementation, audience

### Resumo baseado na transcript

My session is titled Spiffy meet OS federated identity for cloud native workload. I'd like to talk about how Spiffy and OS can work together to build federated identity across modern cloud native platforms especially when workloads and author authorization decisions spans multiple trust domains. From a workload to workload authentication perspective, this problem is largely solved as shown in this figure. Using static client secrets does not scale and introduces operational risk. Identity chaining covers the first two spiffy based client authentication cover the third together they form a completely picture now let's move on the demo we use keyro as an authorization server spire as a spiffy signing authority first let me briefly introduce keyro key In this demo, Aspire provides the workloadies used for OC client authentication via Jot SBIS.

### Excerpt da transcript

Okay. So, hello everyone. Uh, thank you for joining my session. My session is titled Spiffy meet OS federated identity for cloud native workload. I'd like to talk about how Spiffy and OS can work together to build federated identity across modern cloud native platforms especially when workloads and author authorization decisions spans multiple trust domains. Here's today's agenda. First, I'll explain why modern platforms naturally end up with multiple security authorities or what I'll call trust domains and then uh we'll look at what breaks uh when we try to federate identity across those domains especially for user authorization. After that, I'll introduce a standard stand standardsbased approach to securely building federated identity across domains. And finally, I'll show a demo using keyro and spire. Before we dive in, uh let me briefly introduce myself. My name is Yoshik Tabata and I'm a senior OSS consultant. I've spent over 10 years designing and consulting on secure API platforms and identity systems both in enterprise and cloudnative environments and I'm active in the CNSF community uh currently serving as a tech lead for tax and compliance and I'm also a long time longtime contributor to keyro so let's start with the first topic uh modern platforms have multiple security authorities or trust domain A common way of thinking is that a platform has a single security boundary.

In reality, this is a mice. Modern applications span multiple kubernetes clusters, multiple crowds and often multiple organizations. On top of that, we now have tools and AI agents acting as first class participants. Each of these environments performs its own authentication authorization instead of relying on one central authority. In practice, uh both workload identities and user authorization data are issued and evaluated independently in different parts of the system. Spiffy signing authorities issue workload identities and all authorization servers issue tokens that contain scopes and claims. In this talk, I'll treat workload identity and user authorization as separate concerns. To keep things simple, I'll use the term trust domain. A trust domain is the boundary where identity and authorization decisions are made. Across trust domains, nothing is trusted. By default, O and Spiffy define trust domain slightly differently. O focuses on the authorization server as the anchor of trust. Spiffy focuses on the identity name space and its issuing authority in real platforms.

Ho

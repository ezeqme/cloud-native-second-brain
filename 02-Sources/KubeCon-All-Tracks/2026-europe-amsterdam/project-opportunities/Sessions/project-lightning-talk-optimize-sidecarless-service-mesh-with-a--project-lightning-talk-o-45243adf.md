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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Zengzeng Yao", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxw/project-lightning-talk-optimize-sidecarless-service-mesh-with-a-brand-new-rust-based-proxy-zengzeng-yao-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Optimize+Sidecarless+Service+Mesh+With+A+Brand-New+Rust-Based+Proxy+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Optimize Sidecarless Service Mesh With A Brand-New Rust-Based Proxy - Zengzeng Yao, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Zengzeng Yao, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxw/project-lightning-talk-optimize-sidecarless-service-mesh-with-a-brand-new-rust-based-proxy-zengzeng-yao-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Optimize+Sidecarless+Service+Mesh+With+A+Brand-New+Rust-Based+Proxy+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Optimize Sidecarless Service Mesh With A Brand-New Rust-Based Proxy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxw/project-lightning-talk-optimize-sidecarless-service-mesh-with-a-brand-new-rust-based-proxy-zengzeng-yao-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Optimize+Sidecarless+Service+Mesh+With+A+Brand-New+Rust-Based+Proxy+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=knX673N1jKM
- YouTube title: Project Lightning Talk: Optimize Sidecarless Service Mesh With A Brand-New Rust-Base... Zengzeng Yao
- Match score: 0.994
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-optimize-sidecarless-service-mesh-with-a-brand/knX673N1jKM.txt
- Transcript chars: 3185
- Keywords: performance, mesh, waypoint, envoy, optimize, engine, kernel, ebpf, complex, memory, safety, baggage, huawei, massive, overhead, latency, delivers, native

### Resumo baseado na transcript

Uh I'm Yaoenzen from Huawei and my topic today is optimize site color service mesh with a brand new rust based uh proxy. As we know, traditional side car match paved the way, but they brought a heavy trade-offs, tight tight application coupling, massive resources overhead at scale and latency from extra network hoops. And third, the architecture challenger wasn't built for to deeply integrate with EVPF in ancal uh world. Orion proxy is a high performance and memory safe implementation of proxy. Uh when designing Orion, we made a conscious choice not to implement every single envoy API and filter. Orion delivers 2x to 4x high performance, highest throughput along with dramatical early lower latency.

### Excerpt da transcript

Hello everyone. Uh I'm Yaoenzen from Huawei and my topic today is optimize site color service mesh with a brand new rust based uh proxy. As we know, traditional side car match paved the way, but they brought a heavy trade-offs, tight tight application coupling, massive resources overhead at scale and latency from extra network hoops. To solve this uh problem, we built K mesh, an EVPF based cycles traffic management engine that delivers high performance with low overhead. K mash has two has two modes uh kernel native for absolute best performance and the dual engine mode. Today we are diving into the dual engine mode by offloading L4 uh to the kernel and keeping L7 in user space. Uh it provides the the perfect balance of versatility and the performance for most environments. Let's jump in. uh kash and sardis but we still need L4 L7 processing enter the waypoint proxy ebpf handle L4 uh at native speeds and we only route complex L7 uh tasks to the waypoint if it's necessary currently we use Mboy as our waypoint is an amazing project but looking ahead presents uh three hurdles for us first it has returned in C++ uh carrying inherent memory safety risks.

Second, it has heavy and complex uh due to years of historical baggage. And third, the architecture challenger wasn't built for to deeply integrate with EVPF in ancal uh world. So we built Orion in Huawei. Orion proxy is a high performance and memory safe implementation of proxy. Orion is implemented in Rust using high quality open source components. Uh when designing Orion, we made a conscious choice not to implement every single envoy API and filter. Uh while envoying is powerful, it has also massive, highly complex and carries some legacy baggage uh that most modern mesh uh simply don't need. Instead, we took a programmatic approach. Uh we implemented only the essential APIs and filters. Uh this laser folks uh keeps Orion incredibly lightweight, uh simple to maintain, and uh highly performant. To validate our approach, we ran comprehensive benchmarks comparing Orion directly against Envoy. Uh the results clearly shows the payoff of a simple design. Orion delivers 2x to 4x high performance, highest throughput along with dramatical early lower latency.

In the near future, Orion is Kash purposebuilt raster replacement for Envoy as L7 waypoint proxy. Compared to Envoy, the key advantages uh are performance, memory safety and the much lighter footprint and the freedom to optimize specific specifically for the K

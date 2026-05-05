---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["Observability", "Platform Engineering"]
speakers: ["Kasper Borg Nissen", "Developer Relations Engineer", "Dash0"]
sched_url: https://kccnceu2025.sched.com/event/1txBd/keynote-the-observability-platform-engineering-advantage-from-zero-code-to-monitoring-as-code-kasper-borg-nissen-developer-relations-engineer-dash0
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+The+Observability+Platform+Engineering+Advantage%3A+From+Zero-Code+to+Monitoring+as+Code+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: The Observability Platform Engineering Advantage: From Zero-Code to Monitoring as Code - Kasper Borg Nissen, Developer Relations Engineer, Dash0

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Observability]], [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Kasper Borg Nissen, Developer Relations Engineer, Dash0
- Schedule: https://kccnceu2025.sched.com/event/1txBd/keynote-the-observability-platform-engineering-advantage-from-zero-code-to-monitoring-as-code-kasper-borg-nissen-developer-relations-engineer-dash0
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+The+Observability+Platform+Engineering+Advantage%3A+From+Zero-Code+to+Monitoring+as+Code+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: The Observability Platform Engineering Advantage: From Zero-Code to Monitoring as Code.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txBd/keynote-the-observability-platform-engineering-advantage-from-zero-code-to-monitoring-as-code-kasper-borg-nissen-developer-relations-engineer-dash0
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+The+Observability+Platform+Engineering+Advantage%3A+From+Zero-Code+to+Monitoring+as+Code+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Il8fmTzsTEc
- YouTube title: Keynote: The Observability Platform Engineering Advantage: From Zero-Code to Mo... K.B. Nissen (ISL)
- Match score: 0.956
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-the-observability-platform-engineering-advantage-from-zero-cod/Il8fmTzsTEc.txt
- Transcript chars: 15627
- Keywords: instrumentation, application, observability, metrics, without, operator, course, platform, tracing, cluster, obserability, define, applications, engineering, traces, together, source, dashboard

### Resumo baseado na transcript

It's truly an a privilege to be here today, especially as this marks my final time as co-chair for CubeCon, Cloud Native Con. It's been an incredible journey and I couldn't think of a better way to wrap it up than here in London with all of you. It has become the def facto standard for distributed tracing and now extends to logs and metrics as well. Its semantic conventions uh standardizes naming across traces, metrics and logs enabling automatic correlation and reducing inconsistencies between services. And the open telemetry collector um its architecture supports flexible pipelines allowing teams to uh customize their telemetry uh and how they should use it. I'll we'll deploy these services and demonstrate all instrumentation using the open telemetry operator and telemetry will be sent to Prometheus and to for metrics and JGA for tracing.

### Excerpt da transcript

Hi again everyone. It's truly an a privilege to be here today, especially as this marks my final time as co-chair for CubeCon, Cloud Native Con. It's been an incredible journey and I couldn't think of a better way to wrap it up than here in London with all of you. So, let's talk a little bit about observability. For years, we relied on the three pillars of observability, logs, traces, and metrics. But here's the thing, we don't have a metrics problem or tracing problem. We have a systems problem. And yet, many of us still treat these as separate entities. We have one browser tabs for logs, one for metrics, and on a third one for tracing and we relying on humans to correlate signals together. It's inefficient. It's errorprone and it's not how modern obsibility should work. So many teams settle for a good enough approach. And observability is often an afterthought, but it shouldn't be. And this fragmentation leads to multiple challenges. We have many different systems rely on complex security languages making it difficult to unify insights.

The vendor plug-in restricts flexibility and causes barriers to switching tools. Metadata inconsistency across platforms results in unreliable correlations. And due to high complexity, many teams avoid instrumentation all together, leading to gaps in visibility. And with no unified insights, troubleshooting remains slow and inefficient, forcing engineers to manually piece together information across desperate systems. So a shift is happening. It's a shift toward correlation. It's a shift toward standardization. It's a shift toward open telemetry. This is where the community really comes together. Open telemetry or hotel for short. It's a CNCF project and is now the second largest project within the CNCF by contributor account. It has become the def facto standard for distributed tracing and now extends to logs and metrics as well. Open telemetry eliminates proprietary agents, reduces metadata fragmentation and enables cross signal correlation. And it brings four key advantages. First, instrument once, write your instrument instrumentation once and it works across any back end without breaking changes.

Second, it separates telemetry generation from analysis. Open telemetry then ensures that telemetry is produced independently from the tools that are analyzing it. And this allows teams to switch platforms without reinstmenting while vendors focus on analytics instead of this proprietary uh instrumentation. And third, it m

---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/testing-kubernetes-apps-observability-end-to-end/
youtube_url: https://www.youtube.com/watch?v=kDMdGLkRrF8
youtube_search_url: https://www.youtube.com/results?search_query=Testing+Kubernetes+apps%27+observability+end-to-end+PromCon+2023
video_match_score: 1.011
status: video-found
---

# Testing Kubernetes apps' observability end-to-end

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/testing-kubernetes-apps-observability-end-to-end/
- YouTube: https://www.youtube.com/watch?v=kDMdGLkRrF8

## Resumo

Speaker(s): João Pedro Machado Vilaça This presentation is designed for developers and DevOps engineers with a basic understanding of Kubernetes, Prometheus, and alerting concepts. We will cover how to end-to-end test observability features in Kubernetes applications using Prometheus, AlertManager, and various testing frameworks and libraries. We will demo how to set up a test environment, spin up a disposable local cluster, and use Prometheus client libraries for testing.

## Abstract oficial

Speaker(s): João Pedro Machado Vilaça

This presentation is designed for developers and DevOps engineers with a basic understanding of Kubernetes, Prometheus, and alerting concepts. We will cover how to end-to-end test observability features in Kubernetes applications using Prometheus, AlertManager, and various testing frameworks and libraries. We will demo how to set up a test environment, spin up a disposable local cluster, and use Prometheus client libraries for testing. Then, we will see how to write tests for Metrics and Events to ensure their availability and correctness, which are essential to monitoring the application's behavior and diagnosing issues. Next, we will focus on Alert testing. Our primary goal is to understand how to test Alerts for accuracy and timeliness, as alerting is one of the critical components of observability. We will discuss how to ensure our alerts are actionable, relevant, and real, and show how to configure them correctly and ensure they react to the appropriate triggering conditions.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/testing-kubernetes-apps-observability-end-to-end/
- YouTube: https://www.youtube.com/watch?v=kDMdGLkRrF8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kDMdGLkRrF8
- YouTube title: PromCon 2023 - Testing Kubernetes Apps’ Observability End-to-End
- Match score: 1.011
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/testing-kubernetes-apps-observability-end-to-end/kDMdGLkRrF8.txt
- Transcript chars: 22507
- Keywords: alerts, operator, create, actually, metric, metrics, cluster, usually, simple, testing, conditions, validate, already, virtual, clusters, everything, basically, operators

### Resumo baseado na transcript

[Music] [Applause] so hello everyone my name is Jan I'm a software engineer at heet and I'm thrilled to be here today to talk about a topic that is crucial to the health and performance of kubernetes applications but even applications in general testing observability features as developers as devop and devops Engineers we understand the importance in of monitoring our applications right that's why we are here diagnosing issues and ensuring our alerts are accurate and timely so today we'll valve into how we can achieve this using pritus

### Excerpt da transcript

[Music] [Applause] so hello everyone my name is Jan I'm a software engineer at heet and I'm thrilled to be here today to talk about a topic that is crucial to the health and performance of kubernetes applications but even applications in general testing observability features as developers as devop and devops Engineers we understand the importance in of monitoring our applications right that's why we are here diagnosing issues and ensuring our alerts are accurate and timely so today we'll valve into how we can achieve this using pritus alert managers and various testing Frameworks and libraries first a little bit about my work I'm contributing to the CU open source project for those of you that don't know cuir proposes to allow us to hun virtual machines and as native workloads on kubernetes clusters um nowadays I'm participating in cuir with most focus on observability features in the project so uh moving forward I'll present you the agenda um I'll start with how to set up a test environment and what it should look like then we'll start to talk a little bit about AO test metrics from there I'll to ensure that our alerts are are actionable relevant and real then a to test the same alerts and I'll show you a little bit of demo SL showcase so starting up on how to set up the testing environment uh first let's try to understand what these test environment should look like probably most of you already used tools like this right I'm uh a while ago somebody asked how many of you were using kubernetes and most of you were so these tools are probably very familiar but the idea here is that we want to like simulate conditions that approach our production environments but in a controlled space right without the risk of causing disruptions to actual users or developers that might be using a Dev or a staging environment um that's because in our tests we want to um like mess with everything right we want to delete resources create different resources remove permission cause network issues so and this is where the concept of a disposable cluster comes into play these disposable clusters is basically a temporary kubernetes CL cluster that you can create just the for the purpose of the testing the beauty of this approach is that you can spin a cluster you run the test and you just te it down once you're done most of the times they are really shap and um quick quick to set up and we can ensure that we always start the tests with a clean slate we don't have to worry about a

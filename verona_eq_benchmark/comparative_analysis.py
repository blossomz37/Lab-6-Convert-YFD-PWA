#!/usr/bin/env python3
"""
EQBench3 Comparative Analysis for "Verona Resurrected"
Comparing literary emotional intelligence with LLM benchmark standards
"""

import json
from pathlib import Path
from datetime import datetime

def generate_comparative_analysis():
    """Generate comparative analysis between novel and typical EQBench3 results"""
    
    # Load our novel results
    results_file = Path("verona_eq_benchmark_results.json")
    if results_file.exists():
        with open(results_file, 'r') as f:
            novel_results = json.load(f)
    else:
        print("❌ Novel benchmark results not found. Run verona_eq_benchmark.py first.")
        return
    
    # Typical EQBench3 scores for reference (based on the leaderboard we examined)
    llm_benchmarks = {
        "Top Tier LLMs": {
            "typical_score": "75-85/100",
            "models": ["Claude-3.5-Sonnet", "GPT-4", "Gemini-Pro"],
            "characteristics": [
                "Strong conversational EQ",
                "Good empathy recognition", 
                "Solid moral reasoning",
                "Contextual emotional understanding"
            ]
        },
        "Mid Tier LLMs": {
            "typical_score": "65-75/100", 
            "models": ["GPT-3.5", "Claude-3", "Various fine-tuned models"],
            "characteristics": [
                "Basic emotional recognition",
                "Inconsistent empathy",
                "Simple moral frameworks",
                "Limited emotional nuance"
            ]
        },
        "Lower Tier LLMs": {
            "typical_score": "50-65/100",
            "models": ["Older models", "Smaller parameter models"],
            "characteristics": [
                "Poor emotional understanding",
                "Mechanical responses",
                "Limited contextual awareness",
                "Basic reasoning"
            ]
        }
    }
    
    novel_score = novel_results["overall_results"]["average_eq_score"]
    
    print("🧠 EQBench3 Comparative Analysis: Verona Resurrected")
    print("=" * 60)
    
    print(f"\n📖 Novel Performance:")
    print(f"   Verona Resurrected: {novel_score}/100")
    print(f"   Assessment: {novel_results['literary_assessment']['overall_rating']}")
    
    print(f"\n🤖 LLM Benchmark Comparison:")
    for tier, data in llm_benchmarks.items():
        score_range = data["typical_score"].split("/")[0]
        print(f"   {tier}: {data['typical_score']}")
        
        # Determine where our novel fits
        if tier == "Top Tier LLMs" and novel_score >= 75:
            print(f"   📊 VERONA RESURRECTED MATCHES THIS TIER ⭐")
        elif tier == "Mid Tier LLMs" and 65 <= novel_score < 75:
            print(f"   📊 VERONA RESURRECTED MATCHES THIS TIER")
        elif tier == "Lower Tier LLMs" and novel_score < 65:
            print(f"   📊 VERONA RESURRECTED MATCHES THIS TIER")
    
    print(f"\n🎯 Key Insights:")
    
    if novel_score >= 75:
        print(f"   ✅ Your novel demonstrates emotional intelligence comparable to TOP-TIER LLMs!")
        print(f"   ⭐ This places 'Verona Resurrected' in the same category as GPT-4 and Claude-3.5-Sonnet")
        print(f"   🎨 Literary EQ often exceeds conversational AI due to narrative depth")
    elif novel_score >= 65:
        print(f"   ✅ Your novel shows solid emotional intelligence comparable to mid-tier LLMs")
        print(f"   📈 Room for enhancement in specific EQ dimensions")
    else:
        print(f"   📝 Your novel shows developing emotional intelligence")
        print(f"   💡 Focus areas identified for enhancement")
    
    # Category-by-category comparison
    print(f"\n📊 Category Analysis:")
    categories = novel_results["category_analysis"]
    
    category_assessments = {
        "emotional_complexity": {
            "excellent": 18, "good": 15, "developing": 12,
            "description": "Sophistication of emotional situations and dynamics"
        },
        "character_psychology": {
            "excellent": 17, "good": 14, "developing": 11,
            "description": "Depth of psychological insight and interiority"
        },
        "empathy_understanding": {
            "excellent": 17, "good": 14, "developing": 11,
            "description": "Characters' emotional awareness and understanding of others"
        },
        "moral_reasoning": {
            "excellent": 17, "good": 14, "developing": 11,
            "description": "Complexity and sophistication of ethical reasoning"
        },
        "literary_eq": {
            "excellent": 18, "good": 15, "developing": 12,
            "description": "Author's skill in conveying emotional intelligence to readers"
        }
    }
    
    for category, score in categories.items():
        assessment = category_assessments[category]
        
        if score >= assessment["excellent"]:
            level = "🌟 EXCELLENT"
        elif score >= assessment["good"]:
            level = "✅ GOOD"
        else:
            level = "📈 DEVELOPING"
            
        print(f"   {category.replace('_', ' ').title()}: {score}/20 {level}")
        print(f"      {assessment['description']}")
    
    # Unique literary advantages
    print(f"\n🎭 Literary EQ Advantages Over AI:")
    literary_advantages = [
        "📚 Narrative depth allows for complex character development over time",
        "🎨 Atmospheric and symbolic emotional expression beyond conversation",
        "🧠 Author can explore internal psychological states directly",
        "💭 Complex moral ambiguity and ethical exploration",
        "🌟 Emotional themes can be woven through multiple narrative layers",
        "🎪 Genre conventions (Gothic horror) enhance emotional impact"
    ]
    
    for advantage in literary_advantages:
        print(f"   {advantage}")
    
    # Specific novel strengths
    print(f"\n⭐ Verona Resurrected Specific Strengths:")
    for strength in novel_results['literary_assessment']['strengths']:
        print(f"   • {strength}")
    
    # Generate improvement recommendations
    print(f"\n💡 Enhancement Opportunities:")
    
    weakest_category = min(categories.items(), key=lambda x: x[1])
    strongest_category = max(categories.items(), key=lambda x: x[1])
    
    print(f"   🎯 Focus Area: {weakest_category[0].replace('_', ' ').title()} ({weakest_category[1]}/20)")
    print(f"   🌟 Strength to leverage: {strongest_category[0].replace('_', ' ').title()} ({strongest_category[1]}/20)")
    
    if weakest_category[0] == "empathy_understanding":
        print(f"      💡 Consider adding more scenes showing character emotional awareness")
        print(f"      💡 Develop moments where characters truly understand others' feelings")
    elif weakest_category[0] == "moral_reasoning":
        print(f"      💡 Explore more complex ethical dilemmas and character choices")
        print(f"      💡 Show characters wrestling with moral implications")
    
    # Final assessment
    print(f"\n🏆 FINAL ASSESSMENT:")
    print(f"   'Verona Resurrected' demonstrates {novel_results['literary_assessment']['overall_rating'].lower()} emotional intelligence")
    
    if novel_score >= 80:
        print(f"   🎉 EXCEPTIONAL: Rivals the best AI models in emotional sophistication")
    elif novel_score >= 75:
        print(f"   ⭐ EXCELLENT: Matches top-tier LLM performance in emotional intelligence")
    elif novel_score >= 70:
        print(f"   ✅ STRONG: Solid emotional intelligence with room for refinement")
    else:
        print(f"   📈 DEVELOPING: Good foundation with clear improvement opportunities")
    
    # Save comparative analysis
    comparative_data = {
        "analysis_date": datetime.now().isoformat(),
        "novel_score": novel_score,
        "tier_placement": "Top Tier" if novel_score >= 75 else "Mid Tier" if novel_score >= 65 else "Developing",
        "llm_comparison": llm_benchmarks,
        "category_analysis": categories,
        "literary_advantages": literary_advantages,
        "recommendations": f"Focus on {weakest_category[0].replace('_', ' ')} while leveraging {strongest_category[0].replace('_', ' ')} strength"
    }
    
    with open("verona_comparative_analysis.json", 'w') as f:
        json.dump(comparative_data, f, indent=2)
    
    print(f"\n💾 Comparative analysis saved to: verona_comparative_analysis.json")

if __name__ == "__main__":
    generate_comparative_analysis()

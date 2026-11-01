#!/usr/bin/env python3
"""Proxy-Seller ISP & Dedicated SOCKS5 Subnet Calculator 2026."""
import argparse

def calculate(ip_count=20, duration_months=3, promo_discount_pct=15):
    # Proxy-Seller dedicated ISP proxies start around $2.50/IP/mo for US/UK/DE.
    # Term discounts: 1 mo (0%), 3 mos (3%), 6 mos (5%), 12 mos (10%).
    base_rate_per_ip = 2.50
    term_discount = 0.03 if duration_months == 3 else (0.05 if duration_months == 6 else (0.10 if duration_months >= 12 else 0.0))
    
    subtotal_monthly = ip_count * base_rate_per_ip
    discounted_monthly = subtotal_monthly * (1.0 - term_discount)
    gross_total = discounted_monthly * duration_months
    promo_savings = gross_total * (promo_discount_pct / 100.0)
    net_total = gross_total - promo_savings
    effective_rate_per_ip = net_total / (ip_count * duration_months)

    print("=" * 65)
    print("Proxy-Seller Dedicated ISP & SOCKS5 Subnet Calculator")
    print("=" * 65)
    print(f"Allocated Static IPs:      {ip_count} dedicated IPs")
    print(f"Contract Duration:         {duration_months} months (Term discount: {int(term_discount*100)}%)")
    print(f"Standard Base Outlay:      ${subtotal_monthly * duration_months:.2f}")
    print(f"Coupon Discount ({promo_discount_pct}%):     ${promo_savings:.2f}")
    print(f"Net Total Investment:      ${net_total:.2f}")
    print(f"Effective Cost per IP:     ${effective_rate_per_ip:.2f} / IP / month")
    print("=" * 65)
    return net_total, effective_rate_per_ip

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proxy-Seller Pricing Calculator")
    parser.add_argument("--ips", type=int, default=20)
    parser.add_argument("--months", type=int, default=3)
    parser.add_argument("--discount", type=int, default=15)
    args = parser.parse_args()
    calculate(ip_count=args.ips, duration_months=args.months, promo_discount_pct=args.discount)

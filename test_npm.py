from core.checkers.npm_checker import NPMChecker

checker = NPMChecker()

# Test 1: Valid package (should work)
print("Testing valid package...")
try:
    pkg = checker.check_package('react')
    print(f"✅ Success: {pkg.name} v{pkg.version}")
    print(f"   Maintainer: {pkg.maintainer}")
    print(f"   Last updated: {pkg.last_updated}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 2: Invalid package (should fail gracefully)
print("\nTesting invalid package...")
try:
    pkg = checker.check_package('this-does-not-exist-xyz123')
    print(f"✅ Success: {pkg.name}")
except Exception as e:
    print(f"✅ Handled error: {e}")